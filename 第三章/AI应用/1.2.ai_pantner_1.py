import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)



#保存会话信息的函数
def save_session():
    if st.session_state.current_session:
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

    # 如果sessions 目录不存在,创建出来
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

    # 保存会话
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


#加载所有会话信息列表
def load_sessions():
    session_list = []
    # 加载sessions 目录下的文件
    if os.path.exists("sessions"):
        file_list =  os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
        session_list.sort(reverse=True)
        return session_list

def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
                st.session_state.messages = session_data["messages"]
    except Exception :
        st.error("加载会话失败!")

def delete_session(session_name):
    try:
       if os.path.exists(f"sessions/{session_name}.json"):
           os.remove(f"sessions/{session_name}.json")
           if session_name == st.session_state.current_session:
               st.session_state.messages = []
               st.session_state.current_session =generate_session_name()
    except Exception :
        st.error("删除会话失败!")





#大标题
st.title("AI智能伴侣")
#logo
st.logo("🤖")

#ai系统提示词
system_prompt ="""
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1，每次只回1条消息
            2.禁止任何场景或状态描述性文字
            3.匹配用户的语言
            4.回复简短，像微信聊天一样
            5.有需要的话可以用分等emoji表情
            6.用符合伴侣性格的方式对话
            7.回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
        """

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#声明昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小红"

#声明性格
if "nature" not in st.session_state:
    st.session_state.nature= "活泼开朗的南方姑娘"

#会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#展示聊天信息
st.text(f"当前会话标识:{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


#侧边栏 with--streamlit中的上下文管理器
with st.sidebar:
    st.subheader("AI控制面板")
    #新建会话按钮
    if st.button("新建会话",width="stretch",icon="🦴"):
         #保存当前会话信息
        save_session()
        #创建新的会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            st.rerun()

    #增加会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        # st.button(sesssion, width="stretch",icon="📄")
        # st.button("", width="stretch",icon="❌️")
        col1,col2 = st.columns([4,1])
        with col1 :
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("", width="stretch",icon="❌️",key=f"del_{session}"):
                delete_session(session)
                st.rerun()

    #分隔线
    st.divider()
    
    st.subheader("伴侣信息")
    nick_name = st.text_input("请输入伴侣昵称",value=st.session_state.nick_name,placeholder="请输入昵称")
    nature = st.text_input("性格",value=st.session_state.nature,placeholder="请输入性格")

    if nick_name:
        st.session_state.nick_name = nick_name

    if nature:
        st.session_state.nature = nature


#聊天信息输入框
prompt = st.chat_input("输入你要问的问题")
if prompt: #字符串会自动转化为布尔值，非空字符串为True
    st.chat_message("user").write(prompt)
    print("--------->调用大模型,提示词:",prompt)
    st.session_state.messages.append({"role":"user","content":prompt})


    #调用大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="low",  # 推理强度最低
        extra_body={"thinking": {"type": "disabled"}}
    )
    # 大模型返回的结果(流式输出的解析方式)
    full_response  =""
    response_message = st.empty() # 创建一个空的占位符用于显示大模型返回结果
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    # 大模型返回的结果(非流式输出的解析方式)
    # print("<---------大模型返回结果:", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state.messages.append({"role":"assistant","content":full_response})

    #保存会话信息
    save_session()
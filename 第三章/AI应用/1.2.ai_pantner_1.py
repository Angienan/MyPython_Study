import streamlit as st
import os
from openai import OpenAI
from openai.types.containers import file_list_response

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

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

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


#侧边栏 with--streamlit中的上下文管理器
with st.sidebar:
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
import streamlit as st
import os
from openai import OpenAI
st.set_page_config(

    page_title = "AI智能伴侣",
    page_icon="🤖",
    layout = "wide",
    initial_sidebar_state = "expanded",
    menu_items = {}
)

#大标题
st.title("AI智能伴侣")
#logo
st.logo("🤖")


#系统提示词
system_prompt = "你是一名理性的AI助手,你的名字叫李华，请用理性的态度回答用户的问题"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

#创建与AI大模型交互的客户端对象
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
#用户输入
user_prompt = st.chat_input("请输入你要问的问题")
if user_prompt:
    st.chat_message("user").write(user_prompt)
    print("user输入：", user_prompt)
    #将用户输入添加到聊天信息中
    st.session_state.messages.append({"role": "user", "content": user_prompt})

#调用大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "user", "content": user_prompt},
            {"role": "system", "content": system_prompt}
        ],
        stream=True,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "disabled"}}
    )

    #大模型流式输出返回结果
    response_message = st.empty()
    full_response=""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(content)
    #将AI大模型的返回结果添加到聊天信息中
    st.session_state.messages.append({"role": "assistant", "content": full_response})

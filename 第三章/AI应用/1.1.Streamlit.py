"""
Streamlit是一个开源的Python库,专门为数据工程师以及机器学习工程师设计,用来快速基于Python代码构建交互式的web网站(无需掌握前端技术)
安装 pip install streamlit
运行 : streamlit run XXX.py
"""
import streamlit as st

#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落
st.write("我是你的ai智能助手,名字叫王明,我是你理性忠实的好朋友")
st.write("红红火火恍恍惚惚红红火火恍恍惚惚")

#图片
st.image("resources/人1.webp")

#音频
# st.audio("")
#
# #视频
# st.video("")
#
# #logo
# st.logo("")


#表格
student_data = {
    "姓名":["王林","李牧","贝罗"],
    "学号":["123","124","125"],
    "语文":[12,34,76]
}
st.table(student_data)

#输入框
name= st.text_input("请输入姓名:")
st.write("你的姓名:",name)

password= st.text_input("请输入密码:",type="password")
st.write("你的姓名:",password)


#单选按钮
gender = st.radio("输入你的性别",["男","女","未知"],index=2)
st.write(gender)
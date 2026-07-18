"""
PyPI (Python Package index)仓库
按照命令: pip install openai //pip 是Python官方提供的Python包的管理工具,提供了Python包的查看,下载,安装,卸载等功能

# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)
"""

# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
#创建与ai大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字 值就是API的key)
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#与ai大模型进行交互

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你叫洛克,请用理性的态度回答用户的问题"},
        {"role": "user", "content": "你是谁,你能帮我做什么"},
    ],
    stream=False,
)
#返回大模型输入的结果
print(response.choices[0].message.content)
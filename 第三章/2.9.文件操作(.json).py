"""
.json :  JSON 是软件开发中最常用的数据交换格式,而为了简化JSON数据的处理,在Python标准库中就提供了处理JSON数据的核心模块json

序列化: 将Python对象转换为JSON字符串 json.dump()
反序列化: 将JSON字符串转换为Python对象 json.load()
"""
import json
obj = {
    "name" : "张三",
    "age" : 18,
    "gender" : "男",
    "hobbies" : ["reading","swimming"]
}

with open("D:\\Programming\\Python\\Python_Code\\MyPython_Study\\第三章\\AI应用\\resources\\session.json","w",encoding="utf-8") as f:
    #indent: 缩进,在输出的json数据中添加缩进
    #ensure_ascii: 是否使用ascii编码
    json.dump(obj,f,ensure_ascii=False,indent=2)


with open("D:\\Programming\\Python\\Python_Code\\MyPython_Study\\第三章\\AI应用\\resources\\session.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)



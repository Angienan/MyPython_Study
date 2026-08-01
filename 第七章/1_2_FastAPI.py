"""
FastAPI: 是一个现代,快速,高性能的web框架,用于基于标准的Python类型提示构建的API接口服务

"""
from fastapi import FastAPI

#创建实例
app = FastAPI()

#定义API接口,返回值是API接口返回的数据
@app.get("/") #接口访问路径是/,请求方式是GET
def root():
    return {"message": "Hello World"}

#定义API接口
@app.get("/users")
def get_users():
    return [
        {"username": "john", "email": ""},
        {"username": "alice", "email": ""},
        {"username": "bob", "email": ""}
    ]

#启动服务,uvicorn: python中的轻量级web服务器

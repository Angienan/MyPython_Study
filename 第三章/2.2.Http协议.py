"""
网络模型:
OSI网络模型
TCP/IP 四层网络模型

HTTP 超文本传输协议 (Hyper Text Transfer Protocol)),规定了客户端与服务端之间数据传输的规则
特点: 基于文本的协议,基于请求--响应模型,无状态


请求数据格式:
Post /api/courses HTTP/1.1 请求行(请求方式,资源路径,协议)
Accept:
Accept-Encoding:
Accept-Language:           请求头(格式 key:value)
Content-Length:
Content-Type:

{"phone":"123445565","email":"243242414@qq.com","password":"134"}
                           请求体(请求参数部分,GET方式没有,POST可以有)


请求方式:
POST:请求参数在请求体中,POST请求大小是没有限制的
GET: 请求参数在请求行中,没有请求体, 如:/api/courses?name=Python&status=1 GET请求请求参数大小在浏览器是有限制的



响应数据格式
HTTP/1.1 200    200:客户端请求成功 , 400: 请求参数错误  404:请求资源不存在,或者网址有误 500:服务器错误
Accept:
Accept-Encoding:      响应头:格式 key : value
Accept-Language:

{code:1 ,msg:"success"}    响应体
"""

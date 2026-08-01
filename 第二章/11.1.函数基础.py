#定义函数:
#def 函数名(参数列表):
     # 函数体
     # ......
     # return 返回值
#调用函数
# 函数名(参数)
#参数列表和返回值是可有可无的,函数必须先定义再执行(在调用时,函数内部代码不会执行,只有在调用时执行)

# def out_line():
#     print("________________")
# out_line()
#
# def circle_area(r):#(形参)
#     area = 3.14 * r * r
#     return area
#
# print(circle_area(10))
#
# def rectangle_area(l,w):
#     area = l * w
#     return area
# print(rectangle_area(10,5)) #(实参)

# #函数说明文档
# def circle_area_len(r):
#     """
#      多个返回值用逗号分割--封装到元组之中
#     :param r: 圆的半径
#     :return: 圆的面积,圆的周长
#     """
#     return 3.14*r**2 ,round(2*3.14*r,1)
# print(circle_area_len(5))
# print(help(circle_area_len))

# def function_a():
#     print("a..before")
#     function_b()
#     print("a..after")
# def function_b():
#     print("b..before")
#     function_c()
#     print("b..after")
# def function_c():
#     print("c....")
#
# function_a()


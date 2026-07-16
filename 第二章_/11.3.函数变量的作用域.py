# 函数内部的变量叫局部变量,函数外叫全局变量
#函数外部无法访问函数与内部的变量,所以num=1000
#在函数中想使用全局变量,使用global关键字,先声明再使用
num = 100
def circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    global num
    num = 1000
    print("num=",num)
    return area

c_area = circle_area(num)
print(c_area)
print(num)

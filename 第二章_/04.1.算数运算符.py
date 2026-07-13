"""
加:+
减:-
乘:*
除:/(结界为浮点数)
整除://(结果为整数)
求余:%
幂运算:**
"""

#算数运算符优先级
# ** , * ,/ ,// ,% ,+ .-

# 案例0
x = float(input("输入x:"))
y = float(input("输入y:"))
print(f"x+y:{x+y},x-y:{x-y}")

#案例1
a = float(input("输入a的值:"))
b = float(input("输入b的值:"))
c = float(input("输入c的值:"))

print(f"a,b,c的平均数为:{(a+b+c)/3}")
#案例2
a1 = float(input("输入梯形的上底:"))
a2 = float(input("输入梯形的下底:"))
h = float(input("输入梯形的高:"))

print(f"梯形的面积为:{((a1+a2)*h)/2}")
#案例3
r = float(input("输入圆的半径:"))
peri = 2*3.14*r
area = 3.14*r**2
print(f"圆的周长是{peri},面积是{area}")
#案例4
weight = float(input("输入你的体重"))
height = float(input("输入你的升高"))
BMI = weight/(height*height)
print("BMI指数是:%s"% BMI)

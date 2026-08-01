
#定义类
# class Car:
#     pass
#
# c1 = Car()
# # 动态的为对象添加属性-->不推荐
# c1.brand ="BMW"
# c1.name = "X5"
# c1.price = 500000
# #__dict__ 是一个特殊属性,用字典的形式储存对象的属性
# print(c1.__dict__)

#类的定义
"""
class 类名:
   def __init__(self,参数列表):
       self.属性名 = 参数值
       self.属性名 = 参数值

对象名 = 类名(参数列表)

// 定义在类外面的称之为函数,定义在类中的函数称之为方法
// __init__ : 初始化方法,对象创建后自动调用,主要设置对象的初始状态
//self : 方法的第一个参数,表示当前创建的实例对象
"""

class Car:
    def __init__(self,c_color,c_brand,c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_price = c_price
        print("属性添加完毕")

c1 = Car("red","BME",50000)
print(c1.__dict__)

c2 = Car("blue","BME",50000)

print(c2.__dict__)


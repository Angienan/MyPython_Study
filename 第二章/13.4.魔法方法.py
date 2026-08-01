"""
魔法方法是指python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如:__init__.
魔法方法不用我们手动调用,Python会在合适的时间自动调用
__init__: 初始化方法
__str__ : 字符串表示的方法
__eq__: 比较两个对象是否相等 (equal)
__lt__ ,__le__ ,__gt__ ,__ge__ : 比较两个对象的大小(lt : 小于  le : 小于等于  gt : 大于  ge : 大于等于 )
"""

class Car:
    def __init__(self,c_color,c_brand,c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_price = c_price
        print("属性添加完毕")


    def running(self):
        print(f"{self.c_color} {self.c_brand} {self.c_price}这辆车在高速行驶")
    def total_price(self,discount,rate =0.1):
        return self.c_price * discount + rate * self.c_price * rate


    #魔法方法
    def __str__(self):
        return f"{self.c_color} {self.c_brand} {self.c_price}"

    def __eq__(self,other):
        return self.c_color == other.c_color and self.c_brand == other.c_brand and self.c_price == other.c_price

    def __lt__(self,other):
        return self.c_price < other.c_price


c1 = Car("red","BME",50000)
print(c1)



c2 = Car("blue","BME",50000)
print(c2)
#
print(c1==c2)
print(c1>c2)

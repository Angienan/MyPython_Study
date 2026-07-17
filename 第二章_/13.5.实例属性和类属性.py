"""
实例对象: 实例属性属于每个集具体对象的属性,每个对象都是独立的  通过实例对象.属性的方式操作
类属性: 类属性是属于类本身的属性,所有实例共享的 通过 类名.属性 的方法操作

通过实例查找属性时,先查找实例属性,实例属性不存在时,再查找类属性
"""
class Car:
    #类属性
    wheel = 4
    tax_rate = 0.1

    def __init__(self,c_color,c_brand,c_price):
        #实例属性
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_price = c_price
        self.wheel = 2
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
print(c1.c_brand)
print(Car.wheel)
print(c1.wheel)



c2 = Car("blue","BME",50000)
print(c2)
#
print(c1==c2)
print(c1>c2)

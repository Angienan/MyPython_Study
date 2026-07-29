"""
封装计算把属性和操作数据的函数放在一起,形成一个独立的单元,并且内部的实现细节,只对我暴漏必要功能的方法

私有: 私有的属性和方法只能在类的内部使用,python中并没有真正的私有机制,约定在私有属性和方法前面加两个__
"""

class Car:
    wheel = 4
    tax_rate = 0.1

    def __init__(self ,c_color,c_brand,c_name,c_owner):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.__owner = c_owner

    def start(self):
        print("启动")

    def stop(self):
        print("停止")


    def __control_fuel(self):
        print("加油")


    def get_owner(self):
        return self.__owner

if __name__ == "__main__":
    car = Car('audi','A6','黑色','我')
    print(car.start())
    print(car.stop())
    print(car.get_owner())

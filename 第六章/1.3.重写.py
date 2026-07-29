"""
继承 : 子类继承父类,就可以获取到父类的属性和方法

"""

class Car:
    wheel = 4
    tax_rate = 0.1

    def __init__(self ,c_color,c_brand,c_name):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
    def start(self):
        print("启动")

    def stop(self):
        print("停止")


    def __control_fuel(self):
        print("加油")



class fuelcar(Car):
    def stop(self):
        Car.stop(self)
        print("油车停止")

class electriccar(Car):


    def stop(self):
        super().stop()
        print("电车停止")


if __name__ == "__main__":
    c1 = fuelcar("red","audi","A6")
    c2 = electriccar("blue","BME",50000)

    c1.stop()

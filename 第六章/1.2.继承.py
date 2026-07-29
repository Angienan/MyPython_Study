"""
继承 : 子类继承父类,就可以获取到父类的属性和方法

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



class fuelcar(Car):
    pass

class electriccar(Car):
    pass


if __name__ == "__main__":
    c1 = fuelcar("red","audi","A6","w1")
    c2 = electriccar("blue","BME",50000)

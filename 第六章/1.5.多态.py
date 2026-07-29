"""
多态 : 指同一个方法有不同的形态,行为,表现
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



def handle_stop(car : Car):
    car.stop()

if __name__ == "__main__":
    handle_stop(Car("red","audi","A6"))
    handle_stop(Car("blue","BME","f"))
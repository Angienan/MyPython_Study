"""
多继承 : 子类继承多父类,就可以获取到多个父类的属性和方法

当一个类默认继承了多个类,默认优先使用第一个父类的同名属性和方法,可以使用类名.__mro_属性或者类名.mro()方法查看顺序
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


class HUAWEI:
    def __init__(self,version= '1.0'):
        self.version = version

    def run(self):
        print(f"欢迎使用HUAWEI")

class wenjie(Car,HUAWEI):
    pass

class fuelcar(Car):
    pass

class electriccar(Car):
    pass


if __name__ == "__main__":

    c = wenjie()
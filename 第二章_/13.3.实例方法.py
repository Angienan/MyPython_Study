import token


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


c1 = Car("red","BME",50000)
print(c1.__dict__)
c1.running()
total = c1.total_price(discount = 0.2,rate= 0.5)


c2 = Car("blue","BME",50000)
print(c2.__dict__)
c2.running()
total1 = c2.total_price(discount = 0.2,rate= 0.5)
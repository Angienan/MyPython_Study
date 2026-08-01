"""
and:并且
or: 或者
not:取反(True 变为 False))
"""

#案例1
num = input("输入一个整数")
n = int(num)

print(f"{n} 在10-20之间:", 10 <= n <= 20)
#案例2
num = input("输入一个整数")
n = int(num)

print(f"{n} 不在10-20之间:", n<10 or n>20)
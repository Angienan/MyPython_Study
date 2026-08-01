# input()---获取键盘上输入的数据

name = input("请输入你的姓名:")
age = input("请输入你的年纪:")

print(f"你的姓名是:{name},你的年纪是:{age}")


# 案例ATM取款
total_money = 10000
password = input("请输入你的密码")
print("密码输入正确")
money = input("输入你的取款金额")
print("取款成功!")
print(f"你的目前余额是:{total_money-int(money)}")

#案例计算器功能
a = input("请输入a的值")
b = input("请输入b的值")

print(f"a+b:{int(a)+int(b)}")
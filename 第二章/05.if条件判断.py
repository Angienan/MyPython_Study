# score = 700
# if score > 680:
#     print("欢迎来清华读书")
#     print("计入大学生活")
# print("-----------")


#案例1
# ok_account = "188888888"
# ok_password = "666888"
# zhanghao = input("输入账号")
# mima = input("输入密码")
#
# if zhanghao == ok_account and mima== ok_password:
#     print("登录成功,进入b站首页...")
# else:
#     print("登录失败,账号或密码错误")
#
#
# #案例2
# year = int(input("输入年份"))
#
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")
#
# #案例3
# a = int(input("请输入数字"))
# if a % 2 == 0:
#     print(f"{a}是偶数")
# else:
#     print(f"{a}是奇数")
#
# #案例4
# age = int(input("请输入你的年纪"))
# if age >= 18:
#     print("已经成年")
# else:
#     print("未成年")
#
# # 案例5
# count = int(input("输入数字"))
# if count > 0 :
#     print(f"{count}是正数")
# elif count < 0:
#     print(f"{count}是负数")
# else:
#     print(f"{count}是0")
#
# # 案例6
# score = int(input("输入你的分数"))
# if score >= 60:
#     print("你及格了")
# else :
#     print("你没有及格")
#
# # 案例7
# username = input("用户名")
# password = input("密码")
# if username == "admin" and password == "666888":
#     print("登录成功")
# elif username == "root" and password == "547527":
#     print("登录成功")
# elif username == "张三" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败")
#
# # 案例8
# score = int(input("输入你的成绩"))
# if score > 85:
#     print("优秀")
# elif 60 < score < 85 :
#     print("及格")
# else:
#     print("不及格")
#
#
# #案例9
# money = float(input("输入你的金额"))
# if money >= 500:
#     money = money * 0.8
#     print(f"折扣后的金额为:{money}")
# elif  300 < money < 500:
#     money = money * 0.9
#     print(f"折扣后的金额为:{money}")
# elif 100 <= money < 300:
#     money = money * 0.95
#     print(f"折扣后的金额为:{money}")
# else:
#     print("无折扣")
#     print(f"折扣后的金额为:{money}")

#案例10
# a = int(input("输入a边的边长"))
# b = int(input("输入b边的边长"))
# c = int(input("输入c边的边长"))
#
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("三角形为等边三角形")
#     elif  a==c or b==a or c==b:
#         print("三角形为等腰三角形")
#     else:
#         print("三角形为普通三角形")
# else:
#     print("不是三角形")
#
# 案例11

num = float(input("输入你的用电度数"))
if num >= 2880 :
    if  num < 4800:
        price =((num - 2880) * 0.5383) + (2880 * 0.4883)
        print("你的用电度大于2880,小于4800")
        print(f"价格为{price}")
    elif num >= 4800 :
        price = ((num-4800) * 0.7883) + ((4800-2880) * 0.5383)+(2880 * 0.4883)
        print("你的用电度大于4800")
        print(f"价格为{price}")

else:
    price  = num * 0.4883
    print("你的用电度小于2880")
    print(f"价格为{price}")
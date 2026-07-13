# for i in range(5):
#     for j in range(5):
#         # print自带换行效果
#         print("* ",end="")
#     print()
# # 案例1
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i} x {j} = {i*j}",end="  ")
#
#     print()
import random

#案例2
# a = int(input("输入直角三角形的边长"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("* ",end="\t")
#     print()

# 案例3
# b = int(input("输入数字金字塔的数字"))
# for i in range(1,b+1):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()
#
# 打印国际象棋棋盘 ■□
# 案例4
# for i in range(8):
#     for j in range(8):
#         if (i+j) % 2 == 0:
#             print("■  ",end="")
#         else:
#             print("□  ",end="")
#     print()
#案例
#continue : 结束当前循环,进入下一轮循环
#break : 跳出当前循环,结束循环

# a = True
# while  a :
#     username = input("用户名")
#     password = input("密码")
#     if username == "" and password == "":
#         print("用户名和密码不能为空")
#         continue
#
#     if username == "admin" and password == "666888":
#         print("登录成功")
#         break
#     elif username == "root" and password == "547527":
#         print("登录成功")
#         break
#     elif username == "张三" and password == "123456":
#         print("登录成功")
#         break
#     else:
#         print("登录失败")


# while True:
#     i = 5
#     while i>0:
#         username = input("用户名")
#         password = input("密码")
#         if username == "" or password == "":
#             print("用户名和密码不能为空")
#             continue
#
#         if username == "admin" and password == "666888":
#             print("登录成功")
#             break
#         elif username == "root" and password == "547527":
#             print("登录成功")
#             break
#         elif username == "张三" and password == "123456":
#             print("登录成功")
#             break
#         else:
#             i-=1
#             if i==0 :
#                 print("登录失败，次数已用尽，禁止登录")
#             else:
#                 print(f"登录失败,还有{i}次登录机会")
#     break

#案例

# random_number = random.randint(1,100)#生成随机数
#
# while True:
#     number = int(input("请输入一个数字"))
#     if number > random_number:
#         print("您输入的数字太大了")
#     elif number < random_number:
#         print("您输入的数字太小了")
#     else:
#         print("您猜对了")
#         break
#
# print("随机生成的数字是:",random_number)

total = 0
for i in range(1,1001):
    if i % 5 == 0 :
        total += i
print(f"1-1000之间五的倍数和是:{total}")


a = 0
k = 0
str = "akiwksjakdiklowiqaamnvbambaxnsjdsjkaaxkjd"
for c in str :
    if c =="a" :
        a+=1
    if c =="k" :
        k+=1
print(f"字符串中有{a}个a,有{k}个k")

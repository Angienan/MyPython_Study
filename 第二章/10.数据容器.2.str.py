#字符串是字符的容器
# 特点:不可变性,有序性,可迭代性
# 索引和list一致
# s = "Hello-Python"
# print(s[4])
# print(s[7])
#
# for i in s:
#     print(i)
#
# print(s[0:3:])

# 常用方法
"""
find()
count()
upper()
lower()
split()
strip()
replace()
startswith()
"""
s = "Hello,World!人生苦短,我用Python"
print(s.find("x"))
print(s.count("用"))
print(s.upper())
print(s.lower())
print(s.split(","))
print(s.strip("H"))
print(s.replace("Python","Java"))
print(s.startswith("Hel"))


#案例
# mail = input("请输入邮箱: ")
# # in 判断子串是否在字符串当中
#
# if  mail.count("@") == 1 and "." in mail:
#     print(mail,"是合法邮箱")
# else:
#     print(mail,"是非法的邮箱")
#
#
#输入一个字符串,判断该字符串是否是回文
# str1 = input("输入字符串:")
# print(str1)
#
# str2 = str1[::-1]
# if str1 == str2:
#     print("是回文")
# else:
#     print("不是回文")
#案例
re_list = []
for i in range(1,11):
    str1 = input(f"输入第{i}个字符串")
    reversed_str1 = str1[::-1]
    upper_str1 = reversed_str1.upper()
    split_str1= upper_str1.split()
    re_list.append(split_str1)
print(re_list)
"""
元组是不可变的,和列表不同,元素不能修改
定义:元组名称 = (元素)
空元组: 名称 = () /名称 = tuple()

方法:
count()
index():查询元素的对于索引位置(第一个)
"""

# t1 = (1,3,4,5,6,7,8,1)
# print(t1)
# print(type(t1))
#
# print(t1[0])
# print(t1[-1])
#
# print(t1[1:5])
#
# print(t1.count(1))
# print(t1.index(7))
#
# t1 = 300
# t2 = tuple()
# # 定义单元素元组,后面加逗号
# t3 = (122,)


#元组的组包与解包
# 组包:将多个值合并到容器中
# 解包:将容器的元素分开
# 组包
# t1 = (5,23,4,5,2)
# t2 = 3,4,5,6
#
# # 解包
# a,b,c,d,e = t1
# print(a)
#
# # (*)扩展解包 *指收集剩余所有元素,最终封装到列表当中
# x,*y,z = t1
# print(y)

#案例1
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)
#
# a =100
# b = 200
# c = 300
# c,a,b = a,b,c
# print(a)
# print(b)
# print(c)

#案例
students = (
("S001","王林",85,92,78),
("S002","李缪晚",54,95,83),
("S003","十三",24,55,85),
("S004","王卓",12,27,83),
("S005","序目",65,78,98),
("S006","徐立功",54,75,87)
)

print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方式1
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t{s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")#.1f: 保留一位小数
# #方式二
for id1,name,chinese1,math1,english in students:
    total = chinese1 +math1 + english
    avg = total / 3
    print(f"{id1} \t{name} \t {chinese1} \t {math1} \t {english} \t {total} \t {avg:.1f}")#.1f: 保留一位小数

chinese_sores = [s[2] for s in students]
math_sores = [s[3] for s in students]
eng_sores = [s[4] for s in students]

print(f"语文最高分:{max(chinese_sores)}, 最低分:{min(chinese_sores)}, 平均分:{(sum(chinese_sores)/len(chinese_sores)):.1f}")
print(f"数学最高分:{max(math_sores)}, 最低分:{min(math_sores)}, 平均分:{(sum(math_sores)/len(math_sores)):.1f}")
print(f"英语最高分:{max(eng_sores)}, 最低分:{min(eng_sores)}, 平均分:{(sum(eng_sores)/len(eng_sores)):.1f}")

print("优秀学生名单如下:")
for id2,name1,chinese2,math2,english1 in students:
    total = chinese2 + math2 + english1
    avg = total / 3
    if avg > 80:
        print(f"学号:{id2}, 姓名{name1}, 平均分 {avg:.1f}")
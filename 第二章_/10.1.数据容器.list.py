# #列表操作
# #定义
# S = [1,1,2,3,4,54,6,76,34,4,"hello",True]
# print(type(S))
#
# # 访问元素
# # 获取
#
# print(S[0])
# print(S[-1])
#
# # 修改
# S[4] = 88
# print(S[4])
# print(S)
#
# # 删除
# del S[4]
# print(S)
#
#
# #遍历
# for item in S :
#     print(item)
#
# #切片
# # S[开始:结束(不包含):步长]
# s = S[0 : 4 : 1]
# print(s)
# s = s[ : 4:2]
# print(s)
#
# s = S[0 : -1]
# print(s)
#git的使用

#列表方法的使用
"""
append():在列表最后一位追加元素
insert():在指定索引添加元素
remove():移除列表第一个匹配到的值
pop(): 删除列表中指定索引的位置,没有指定就默认删除最后一个
sort():对列表进行排序,相同的数据类型
remove():对列表进行反转
"""
from logging.config import listen
from typing import final

#
#
# R  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 11]
# print(R)
# R.insert(0,0)
# print(R)
# R.remove(3)
# print(R)
# R.pop(8)
# print(R)
# R.sort()
# print(R)
# R.reverse()
# print(R)
# # 案例1
# num_list = []
# for i in range(10):
#     num  = int(input("输入数字"))
#     num_list.append(num)
# print("数字列表:",num_list)
#
# num_list.sort()
# print("排序之后的列表",num_list)
#
# print("最大值:",max(num_list))
# print("最小值:",min(num_list))
# #sun()求和,,,len()列表长度
# print("平均值:",sum(num_list)/len(num_list))

# 案例2
#
# num_list1 = [12,3,4,5,62,4,7,45,24,5,6]
# num_list2 = [1,2,3,4,5,6,7,8,9,10]
#
# # 合并列表
# # *解包:将列表这一个容器解开一个一个的元素
# #组包:将多个值合并在一起
#
#
#
# num_list = num_list1 + num_list2
# print(num_list)
# #
# # # 去除重复
# new_list = []
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

# #案例
# # 1-20的平方列表 range(1,21)
# num_list = []
# for num in range(1,21):
#     num_list.append(num**2)
# print(num_list)
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)
#
# #案例
# num_list3 =[3,14,56,324,6,65,73,5,23,423,4,23]
# new_list = [i**2 for i in num_list3 if i%2==0]
# print(new_list)
# #列表推导式 : 按照一定的规则快速生成一个列表方法
# # 语法格式1: [ 插入的值 for i in 序列/列表 ]
# # 语法格式2: [ 插入的值  for i in 序列/列表  if条件]


#需求1
# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']
# new_list = list1 + list2+list3
# print("合并的列表",new_list)
# final_list = []
# for i in new_list:
#     if i not in final_list:
#         final_list.append(i)
# print("去除重复的列表",final_list)
# final_list.sort()
# print("排序后的列表",final_list)
# #需求2
# list1 =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30]
# list2 = [i**2 for i in list1 if i % 3==0 or i % 5 == 0]
# print("新列表:",list2)
#需求三
# list1 = [11,2,31,4,-5,12,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
# list2 = [i for i in list1 if i>0]
# print("新列表",list2)


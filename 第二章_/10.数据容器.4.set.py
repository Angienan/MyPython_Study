#集合set无序,不可重复,可修改的容器
#定义:set{}
# 空集合 s1 = set()  空集合不可以使用{},{}表示空字典,集合是无序的,不支持下标索引
# s1 = {4,3,2,5,6,3,5}
# print(s1)
#
# s2 = set()

"""
set集合常用方法
add() :添加元素到集合
remove():移除指定元素
pop():随机删除一个元素并返回
clear():清空集合
difference():求两个集合的差集
union(): 求两个集合的并集
intersection(): 求两个集合的交集
"""
# s1 = {4,3,2,5,6,3,5}
# s2 = {5.2,67,3,45,52}
# print(s2)
# s1.add(100)
# print(s1)
# s1.remove(100)
# print(s1)
# e =s1.pop()
# print(e)
# print(s1.difference(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))

# 案例#
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}


fa =french_set.intersection(art_set)
print(fa)
# & 求交集
fa2 = french_set & art_set
print(fa2)
all_set =french_set.intersection(art_set,basketball_set,football_set,art_set)
all_set2 = football_set & basketball_set & french_set & art_set
print(all_set)
print(all_set2)

fnol = football_set.difference(basketball_set)
print(fnol)
# -求差集
fnol2 = football_set - basketball_set
print(fnol2)
# 集合推导式
fnol3 = {s for s in football_set  if s not in basketball_set}
print(fnol3)

all_student_set = football_set.union(basketball_set,football_set,french_set,art_set)
all_student_set2 = football_set | basketball_set | french_set | art_set
print(all_student_set)
print(all_student_set2)

all_list = [*football_set,*basketball_set,*french_set,*art_set]
print(all_list)
for s in art_set:
    print(s,"选修了",all_list.count(s) ,"门课程")
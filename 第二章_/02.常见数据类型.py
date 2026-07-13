# 数据类型: 整数 int , 浮点数 float , 字符串 str , 布尔 bool, 空值 NoneType
a = 100
print(type(a))
print(type(122))

print(isinstance(a,int))
# 字符串的三种定义方式:1:双引号定义, 2:单引号定义, 3: 三引号定义
# 1
s1 = "我是s1"

# 2
s2 = '我是s2'

#3
s3 = """
     你好:
     很高兴为您服务
     我是你的助手
"""

print(type(s1))
print(isinstance(s2,str))
print(type(s3))

mas =' It\'s very easy'
print(type(mas))
print(isinstance(mas,str))
print(mas)

s1 = "人生苦短," "我用python"
print(s1)

# 字符串格式化
# 1.使用%s占位符,s指将变量转换为字符串形式
name = "涛哥"
age = 18
study = "软件工程"
hobby = "Python ,Java"
mas = "\"大家好,我是 %s ,今年 %s 岁,学习的专业是 %s,爱好是 %s\"" % (name, age, study, hobby)
print(mas)

# 2.使用f"{变量/表达式}" 推荐
name = "涛哥"
age = 18
study = "软件工程"
hobby = "Python ,Java"
mas = f"大家好,我是{name},今年{age}岁,学习的专业是{study} ,爱好是{hobby}"
print(mas)
print("d")
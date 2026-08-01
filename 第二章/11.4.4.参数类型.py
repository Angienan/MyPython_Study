#普通参数:数字,布尔,字符串,列表,元组,集合,字典
#特殊参数:函数
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def calc(a,b,oper):
    return oper(a,b)

print(calc(2,3,add))
print(calc(2,3,sub))
print(calc(2,3,mul))
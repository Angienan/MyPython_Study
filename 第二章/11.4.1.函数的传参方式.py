#在调用函数时,传递参数的方式:
# 1.位置传参:根据函数形参定义时的位置顺序传递参数
# 2.关键字传参: 形参匹配实参,位置可以变化
# 3.位置传参+关键字传参: 前面必须是位置传参按照定义时的顺序,后面关键字传参
#定义函数
def reg_stu(name,age,gender,city):
    print(f"注册成功 姓名:{name},年纪:{age},性别:{gender},城市:{city}")
    return {'name':name,'age':age,'gender':gender,'city':city}
# 1.位置传参
stu = reg_stu("张三","14","男","北京")
print(stu)

sut2 = reg_stu(name ="王林",city="南京",gender="女",age=18)
print(sut2)

stu3 = reg_stu("李四",20,city="上海",gender=30)
print(stu3)
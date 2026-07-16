# 默认参数也为缺省参数,在调用函数时,可与不传递有默认值的参数
# 默认参数必须放在非默认参数之后
def reg_stu(name,age,gender="男",city="北京"):
    print(f"注册成功 姓名:{name},年纪:{age},性别:{gender},城市:{city}")
    return {'name':name,'age':age,'gender':gender,'city':city}
# 1.位置传参
stu = reg_stu("张三","14")
print(stu)

sut2 = reg_stu(name ="王林",city="南京",gender="女",age=18)
print(sut2)


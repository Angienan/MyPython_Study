# 不定长参数也叫可变参数,用于函数定义以及调用时参数个数的不确定(0或多个)的场景
# 类型:
# 位置传递
# 关键字传递

# 位置传递
#传递的所有参数都会被args变量收集,并且合并封装成元组,arge是元组类型(不能分装关键字)
# args 是约定俗称的变量名,不是关键字,可以使用任意合法的变量名
# def calc_date(*args):
#    max1 = max(args)
#    min1 = min(args)
#    avg1 = sum(args)/len(args)
#    return max1,min1,round(avg1,1)
#
# data1 = calc_date(1,2,3,4,5)
# print(data1)
#
# data2 = calc_date(1,233,14,87,46,56,3,7,634,76,0)
# print(data2)

#关键字传递参数(**kwargs)
#会把键值对封装到字典中
def calc_date(*args,**kwargs):
   max1 = max(args)
   min1 = min(args)
   avg1 = sum(args)/len(args)

   if kwargs.get("round") is not None:
      avg1 = round(avg1,kwargs.get("round"))

   if kwargs.get("print") is not None:
      print("最大值",max1,min1,avg1)


   return max1,min1,round(avg1,1)

data1 = calc_date(1,2,3,4,5,round = 1,print=True)
print(data1)

data2 = calc_date(1,233,14,87,46,56,3,7,634,76,0)
print(data2)
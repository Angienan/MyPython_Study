#本质是一个文件夹,可以包含若干python模块,文件夹下还包含一个 __init__.py(描述当前包的信息)
#当模块比较多时,用来管理多个模块
#包的导入方式
# import 包名.模块名 ,...
# import 包名.模块名 as 别名...
#    导入模块的功能
# from 包名.模块名 import 功能名,...
# from 包名.模块名 import 功能名 as 别名
# from 包名.模块名 import * 导入所有功能
#
#
#
#
#
# 导入模块
# import utils.my_fun
# utils.my_fun.log_separator4()
# from utils import my_fun
# my_fun.log_separator1()
#如果要通过*的方式,需要在在__init__中添加__all__
from utils import *
my_fun.log_separator1()
print(my_var.PI)





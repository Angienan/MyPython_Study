# #导入模块
# import my_fun as mf
# print(mf.log_separator1())
# print(mf.log_separator2())
# print(mf.log_separator3())
# print(mf.PI)

from my_fun import *
print(PI)
log_separator2()
log_separator1()
log_separator3()
print(NAME)

# __all__: 是一个模块级别的特殊变量,用于指定from 模块名 import * 时会导入哪些功能

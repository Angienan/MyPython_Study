"""
module:模块..... 一个.py文件就是一个模块,是Python程序的基本组成单位,在模块中可以定义变量,函数,类,以及可执行的代码
提高代码复用性,降低开发门槛,减少命名
在使用模块提供的功能前,必须先导入
具体语法:
   导入整个模块
import 模块名 ,...
import 模块名 as 别名...
   导入模块的功能
from 模块名 import 功能名,...
from 模块名 import 功能名 as 别名
from 模块名 import * 导入所有功能
"""
# 调用方式:模块名.功能名
# import  random as rnd
# for i in range(10):
#     print(rnd.randint(1,100))
#
# 2.导入模块的功能
from random import *
for i in range(10):
   print(randint(1,100))

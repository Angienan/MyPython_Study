"""
异常(bug)程序运行过程中出现的异常,他会中断程序的正常执行流程
try:
   代码
except [异常类型 as 变量名]:
    出现异常的预案
finally:
    不管出现异常,都会执行
"""

# try:
#     print("=========")
#     print(1/0)
#     print("=========")
# except Exception as e:
#     print("程序报错",e)
#
# finally:
#     print("=========资源释放==========")

#异常的传递就是异常在函数调用中层层上报,直到有人处理他
def fun1():
    print("hello")
    fun2()
def fun2():
    print("hello")
    fun3()
def fun3():
    print("hello")
    print(my)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print(e)
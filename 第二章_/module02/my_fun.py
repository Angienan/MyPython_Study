# 常量的名称全大写

__all__ = ['log_separator1', 'log_separator2', 'log_separator3',"PI","NAME"]
PI = 3.1415926
NAME = "小明"


def log_separator1():
    print("-" * 30)


def log_separator2():
    print("+" * 30)


def log_separator3():
    print("#" * 30)


def log_separator4():
    print("*" * 30)
#__name__ :内置变量,表示当前模块的名字(__name__的值为__main_)
#被当中模块导入,如下代码不执行
if __name__ == '__main__':
    log_separator1()
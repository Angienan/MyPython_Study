#类型注解是一种语法特性,用于明确标识变量,函数参数,返回值的数据类型,从而使代码更加清晰安全
a : int =55
score:float = 98.5
hobby : str = 'python'
names : list[str | int] =["a","b","c"]
phones : set[str]
options  : dict[str,int]
goods : tuple[str,int,int]

names.append(1)
#对变量直接赋值,变量运算等场景:类型推断,Python 解释器会自动推断变量类型,类型注解不会影响运行结果
#Python是动态类型语言,添加类型注解只是提示,不是强制约束
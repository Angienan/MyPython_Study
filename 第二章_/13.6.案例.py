# #学生类
# class Student:
#     def __init__(self, name, chinese,math,english):
#         self.name = name
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#
#     def __str__(self):
#         return f"姓名:{self.name} | 语文成绩:{self.chinese} | 数学成绩:{self.math} | 英语成绩:{self.english} | 总成绩:{self.chinese+self.math+self.english}"
#
#     def update_score(self, chinese = None ,math = None , english = None):
#         if chinese is not None:
#             self.chinese = chinese
#         if math is not None:
#             self.math = math
#         if english is not None:
#             self.english = english
#
# #教务管理系统类
#
# class EduManagement:
#     system_version = "1.0.0"
#     system_name = "学生教务管理系统"
#     def __init__(self):
#         self.student_list = []
#
#     #添加学生成绩
#     def add_student(self):
#         name = input("输入你的姓名")
#
#         for s in self.student_list:
#             if s.name == name:
#                 print("学生信息已经存在")
#             return
#         chinese =int(input("输入你的语文成绩:"))
#         math =int(input("输入你的数学成绩:"))
#         english =int(input("输入你的英语成绩:"))
#
#         if  0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
#             stu = Student(name,chinese,math,english)
#             self.student_list.append(stu)
#         else:
#             print("输入的成绩必修在1-100之间")
#
#     #修改学生成绩
#     def update_student(self):
#         name =input("输入你的姓名:")
#         target_stu = None
#
#         for s in self.student_list:
#             if s.name == name:
#                 target_stu = s
#                 break
#             if target_stu is  None:
#                 print("没有找到该学生")
#                 return
#             print(f"当前成绩：{target_stu}")
#
#         chinese = int(input("输入要修改的语文成绩:"))
#         math = int(input("输入要修改的数学成绩:"))
#         english = int(input("输入要修改的英语成绩:"))
#
#
#         if  0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
#             target_stu.update_score(chinese, math, english)
#             print("成绩修改成功")
#             print(f"更新后成绩：{target_stu}")
#         else:
#             print("输入的成绩必修在1-100之间")
#
#
#
#     #删除学生信息
#     def delete_student(self):
#         name = input("输入你的姓名:")
#         for s in self.student_list:
#             if s.name == name:
#                 self.student_list.remove(s)
#                 print("学生信息删除成功！")
#                 return
#         print("没有找到学生")
#
#     #查询单个学生信息
#     def query_student(self):
#         name = input("输入你的姓名:")
#         for s in self.student_list:
#             if s.name == name:
#                 print(f"学生信息：{s}")
#                 return
#         print("没有找到学生")
#
#     #列出全部的学生信息
#     def all_student(self):
#         if not self.student_list:
#             print("没有任何学生信息")
#             return
#         print("===== 全部学生信息 =====")
#         for s in self.student_list:
#             print(s)
#
#     #系统入口
#     def run(self):
#         print(f"欢迎使用{EduManagement.system_name} V{EduManagement.system_version}")
#         while True:
#             print("\n#####################################################################")
#             print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统 #")
#             print("#####################################################################")
#             op = input("请输入你要执行的操作序号：")
#             match op:
#                 case "1":
#                     self.add_student()
#                 case "2":
#                     self.update_student()
#                 case "3":
#                     self.delete_student()
#                 case "4":
#                     self.query_student()
#                 case "5":
#                     self.list_student()
#                 case "6":
#                     print("感谢使用，系统退出，拜拜！")
#                     break
#                 case _:
#                     print("输入序号错误，请重新输入！")
#
# if __name__ == "__main__":
#     a = EduManagement()
#     a.run()
#
class GoodsInfo:
    def __init__(self,name,price,number):
        self.name = name
        self.price = price
        self.number = number

    def __str__(self):
        return f"商品名称:{self.name}, 商品价格: {self.price},商品数量: {self.number}"

    def update_info(self,name,price,number):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if number is not None:
            self.number = number


class GoodManagement:
    system_version = "1.0.0"
    system_name="购物车管理系统"

    def __init__(self):
        self.goods_info_list = []

    #添加购物车

    def add_goods(self):
        name = input("输入商品名称:")

        for s in self.goods_info_list:
            if s.name == name:
                print("商品已经存在")
            return

        price = float(input("输入商品价格:"))
        number  = int(input("输入商品数量:"))

        goods = GoodsInfo(name,price,number)
        self.goods_info_list.append(goods)


    #修改购物车
    def update_info(self):
        name = input("输入你要修改的商品名称")
        target_goods = None

        for s in self.goods_info_list:
            if s.name == name:
                target_goods = s
                break

            if target_goods is None:
                print("没有找到该学生")
                return
        print("当前商品信息",target_goods)


        price = float(input("输入修改的商品价格:"))
        number = int(input("输入修改的商品数量:"))
        target_goods.update_info(name,price,number)
        print("修改成功")

    #删除购物车
    def delete_goods(self):
        name = input("输入需要删除的商品名称")
        for s in self.goods_info_list:
            if s.name == name:
                self.goods_info_list.remove(s)
                print("删除信息成功")
                return
            print("没有找到这个商品")

    def all_goods(self):
        for s in self.goods_info_list:
            print("列出购物车所有信息")
            print(s)

        if not self.goods_info_list:
            print("购物车没有任何信息")

    def run(self):
        print(f"欢迎使用{GoodManagement.system_name} V{GoodManagement.system_version}")
        while True:
            print("\n#####################################################################")
            print("# 1.添加购物车  2.修改购物车  3.删除购物车    4.查询购物车  5.退出系统 #")
            print("#####################################################################")
            op = input("请输入你要执行的操作序号：")
            try:
                match op:
                    case "1":
                        self.add_goods()
                    case "2":
                        self.update_info()
                    case "3":
                        self.delete_goods()
                    case "4":
                        self.all_goods()
                    case "5":
                        print("感谢使用，系统退出，拜拜！")
                        break
                    case _:
                        print("输入序号错误，请重新输入！")
            except Exception as e:
                print(e)

if __name__ == "__main__":
    a = GoodManagement()
    a.run()
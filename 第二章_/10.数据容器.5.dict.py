# """
# dict字典中存在键值对类型的数据(key : value)) dictionar
# 定义:
# 键值对存储,不能重复,可以修改
#
# 字典名称= {key:value ,key:value ,key:value }
#
# 空字典: 字典名称 ={}/ 字典名称 = dict{}
# 值 = 字典名称[key]
# 字典中的val可以是任意类型,key不能为可以变化的类型
# key可以是str,int ,float,tuple,不能是:list,set,dict
# """
#
# # dict1 = {"王林": 670,"李牧":608}
# # print(dict1)
# # dict2 = {"王林": 670,"李牧":608}
# #
# # #访问
# # print(dict1["王林"])
# # dict1["王林"] = 690
# # print(dict1)
# #
# # dict2 = {"王林": 670,"李牧":608,"李琪":478,"小黑":545,"温韬":429}
# #
# # #不存在就添加
# # dict2["涛哥"] = 688
# # print(dict2)
# # #存在就修改
# # dict2["李牧"] = 888
# # print(dict2)
# #
# # #删除
# # # pop删除并且返回
# # score = dict2.pop("小黑")
# # print(score)
# # del dict2["王林"]
# # print(dict2)
# #
# #
# # #修改
# # #查询
# # print(dict2["李牧"])
# # print(dict2.get("李琪"))
# # print(dict2.keys())
# # print(dict2.values())
# # print(dict2.items())
# #
# # #遍历字典
# # for k in dict2.keys():
# #     print(f"{k}: {dict2[k]}")
# #
# # for k,v in dict2.items():
# #     print(f"{k}: {v}")
# #
#
# shopping_cart = {}
#
# menu = """
# ######购物车系统#######
# #    1.添加购物车     #
# #    2.修改购物车     #
# #    3.删除购物车     #
# #    4.查询购物车     #
# #    5.退出购物车     #
# #####################
# """
# print("欢迎使用购物车系统")
# print(menu)
#
# #接收用户输入
# while True:
#         choice = input("请选择执行的操作(1-5)")
#
#         match choice:
#             case "1":
#                 goods_name = input("请输入商品的名称:")
#                 goods_price = float(input("请输入商品的价格:"))
#                 goods_num = int(input("请输入商品的数量:"))
#             #     如果商品存在,提示
#                 if goods_name in shopping_cart:
#                     print("该商品存在,请重新选择..")
#                 else:
#                     shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
#                     print("添加完成")
#
#             case "2":
#                 goods_name = input("请输入商品的名称:")
#                 goods_price = float(input("请输入商品的价格:"))
#                 goods_num = int(input("请输入商品的数量:"))
#                 #     如果商品存在,提示
#                 if goods_name not in shopping_cart:
#                     print("该商品存在,请重新选择..")
#                 else:
#                     shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                     print("修改完成")
#             case "3":
#                 goods_name = input("请输入商品的名称:")
#                 if goods_name not in shopping_cart:
#                     print("商品不存在,重新选择")
#                 else:
#                     del shopping_cart[goods_name]
#                     print("删除完毕")
#             case "4":
#                 for goods_name in shopping_cart:
#                     goods_info = shopping_cart[goods_name]
#                     print(f"商品名称:{goods_name}, 商品价格:{goods_info['price']}, 商品数量:{goods_info['num']}")
#             case "5":
#                 print("退出购物车")
#                 break
#             case _:
#                 print("非法操作,不支持")
# print("已退出购物车")

student_system = {}

menu = """
########教务管理系统#######
#     1.添加学生信息      #
#     2.修改学生信息      #
#     3.删除学生信息      #
#     4.查询学生信息      #
#     5.列出所有学生      #
#     6.统计班级成绩      #
#     7.退出系统         #
########################
"""
while True:
    print(menu)
    choice = input("输入你要进行的操作(1-7):")

    match choice:
        case "1":
            stu_name = input("输入学生姓名:")
            # 转浮点数字，用于后续成绩统计
            chinese_score = float(input("输入学生语文成绩:"))
            math_score = float(input("输入学生数学成绩:"))
            english_score = float(input("输入学生英语成绩:"))

            if stu_name in student_system:
                print("学生姓名已经存在，录入失败！")
            else:
                student_system[stu_name] = {"语文成绩": chinese_score, "数学成绩": math_score, "英语成绩": english_score}
                print("录入完成")

        case "2":
            stu_name = input("输入学生姓名:")
            chinese_score = float(input("输入学生语文成绩:"))
            math_score = float(input("输入学生数学成绩:"))
            english_score = float(input("输入学生英语成绩:"))
            if stu_name not in student_system:
                print("学生姓名不存在，修改失败")
            else:
                student_system[stu_name] = {"语文成绩": chinese_score, "数学成绩": math_score, "英语成绩": english_score}
                print("修改完成")

        case "3":
            stu_name = input("输入学生姓名:")
            if stu_name not in student_system:
                print("学生不存在，删除失败")
            else:
                del student_system[stu_name]
                print("删除完成")

        case "4":
            stu_name = input("输入学生姓名:")
            if stu_name not in student_system:
                print("该学生不存在")
            else:
                person_info = student_system[stu_name]
                print(f"学生姓名:{stu_name}  语文成绩:{person_info['语文成绩']},数学成绩:{person_info['数学成绩']},英语成绩:{person_info['英语成绩']}")

        case "5":
            if len(student_system) == 0:
                print("暂无学生信息")
                continue
            for all_stu in student_system:
                all_stu_info = student_system[all_stu]
                print(f"学生姓名:{all_stu}  语文成绩:{all_stu_info['语文成绩']},数学成绩:{all_stu_info['数学成绩']},英语成绩:{all_stu_info['英语成绩']}")
            print("学生信息输出完毕")

        case "6":
            if len(student_system) == 0:
                print("暂无学生，无法统计成绩")
                continue
            chinese_list = []
            math_list = []
            english_list = []
            # 先收集全部成绩，再统一计算（移出for循环）
            for name, score in student_system.items():
                chinese_list.append((score["语文成绩"], name))
                math_list.append((score["数学成绩"], name))
                english_list.append((score["英语成绩"], name))

            # 语文统计
            ch_score, ch_name_max = max(chinese_list, key=lambda x: x[0])
            ch_min_score, ch_name_min = min(chinese_list, key=lambda x: x[0])
            ch_avg = sum([i[0] for i in chinese_list]) / len(chinese_list)
            # 数学统计
            ma_score, ma_name_max = max(math_list, key=lambda x: x[0])
            ma_min_score, ma_name_min = min(math_list, key=lambda x: x[0])
            ma_avg = sum([i[0] for i in math_list]) / len(math_list)
            # 英语统计
            en_score, en_name_max = max(english_list, key=lambda x: x[0])
            en_min_score, en_name_min = min(english_list, key=lambda x: x[0])
            en_avg = sum([i[0] for i in english_list]) / len(english_list)

            print("\n========== 班级成绩统计 ==========")
            print(f"【语文】最高分：{ch_score}({ch_name_max}) | 最低分：{ch_min_score}({ch_name_min}) | 平均分：{ch_avg:.2f}")
            print(f"【数学】最高分：{ma_score}({ma_name_max}) | 最低分：{ma_min_score}({ma_name_min}) | 平均分：{ma_avg:.2f}")
            print(f"【英语】最高分：{en_score}({en_name_max}) | 最低分：{en_min_score}({en_min_score}) | 平均分：{en_avg:.2f}")
            print("===================================\n")

        case "7":
            print("退出系统")
            break
        case _:
            print("输入失败,请重新输入1~7之间的数字.")
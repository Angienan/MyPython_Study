"""
dict字典中存在键值对类型的数据(key : value)) dictionar
定义:
键值对存储,不能重复,可以修改

字典名称= {key:value ,key:value ,key:value }

空字典: 字典名称 ={}/ 字典名称 = dict{}
值 = 字典名称[key]
字典中的val可以是任意类型,key不能为可以变化的类型
key可以是str,int ,float,tuple,不能是:list,set,dict
"""

# dict1 = {"王林": 670,"李牧":608}
# print(dict1)
# dict2 = {"王林": 670,"李牧":608}
#
# #访问
# print(dict1["王林"])
# dict1["王林"] = 690
# print(dict1)
#
# dict2 = {"王林": 670,"李牧":608,"李琪":478,"小黑":545,"温韬":429}
#
# #不存在就添加
# dict2["涛哥"] = 688
# print(dict2)
# #存在就修改
# dict2["李牧"] = 888
# print(dict2)
#
# #删除
# # pop删除并且返回
# score = dict2.pop("小黑")
# print(score)
# del dict2["王林"]
# print(dict2)
#
#
# #修改
# #查询
# print(dict2["李牧"])
# print(dict2.get("李琪"))
# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())
#
# #遍历字典
# for k in dict2.keys():
#     print(f"{k}: {dict2[k]}")
#
# for k,v in dict2.items():
#     print(f"{k}: {v}")
#

shopping_cart = {}

menu = """
######购物车系统#######
#    1.添加购物车     #
#    2.修改购物车     #
#    3.删除购物车     #
#    4.查询购物车     #
#    5.退出购物车     #
#####################
"""
print("欢迎使用购物车系统")
print(menu)

#接收用户输入
while True:
        choice = input("请选择执行的操作(1-5)")

        match choice:
            case "1":
                goods_name = input("请输入商品的名称:")
                goods_price = float(input("请输入商品的价格:"))
                goods_num = int(input("请输入商品的数量:"))
            #     如果商品存在,提示
                if goods_name in shopping_cart:
                    print("该商品存在,请重新选择..")
                else:
                    shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
                    print("添加完成")

            case "2":
                goods_name = input("请输入商品的名称:")
                goods_price = float(input("请输入商品的价格:"))
                goods_num = int(input("请输入商品的数量:"))
                #     如果商品存在,提示
                if goods_name not in shopping_cart:
                    print("该商品存在,请重新选择..")
                else:
                    shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                    print("修改完成")
            case "3":
                goods_name = input("请输入商品的名称:")
                if goods_name not in shopping_cart:
                    print("商品不存在,重新选择")
                else:
                    del shopping_cart[goods_name]
                    print("删除完毕")
            case "4":
                for goods_name in shopping_cart:
                    goods_info = shopping_cart[goods_name]
                    print(f"商品名称:{goods_name}, 商品价格:{goods_info['price']}, 商品数量:{goods_info['num']}")
            case "5":
                print("退出购物车")
                break
            case _:
                print("非法操作,不支持")
print("已退出购物车")
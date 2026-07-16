# # 匿名函数,没有名称的函数,需要通过lambda表达式来声明函数,可以简化书写
# #定义匿名函数
# # lambda 参数列表:函数体
# #匿名函数不需要写return
# out_line = lambda : print("__________")
#
# add = lambda x,y : x+y
#
# out_line()
# print(add(199,122))
#
#
# cr_area = lambda r : 3.14*r**2
# print(cr_area(100))
#
#
# data_list = ["1","23","73","46","5","65","7","839","10"]
# print(data_list)
# data_list.sort(key=lambda item:len(item),reverse=True)
# print(data_list)
from functools import total_ordering
from turtledemo.penrose import sun


# 案例1  递归调用:在函数中自己调用自己的情况  一定要有终结点
# def jc(n):
#     if n == 1:
#         return  1
#     else:
#         return n * jc(n-1)
#
# result = jc(10)
# print(result)
#
#

#案例2
def calc_order_cost(*args,coupon=0,score=0,package_money=0):
    """
    根据传入的信息计算价格
    :param args: 商品信息----->元组
    :param coupon: 优惠券
    :param score: 积分
    :param package_money:运费
    :return: 总金额
    """

    # 1.计算商品金额
    total_price =[goods[1]*goods[2] for goods in args]
    total_cost = sum(total_price)
    #2.减扣优惠券
    if total_cost>=5000 and coupon <= total_cost:
        total_cost -= coupon

    if total_cost >= 5000 and score // 100 <= total_cost :
        total_cost -= score // 100

    total_cost += package_money

    return total_cost


total =  calc_order_cost(("鼠标",155,2),("车",388,5),coupon=100,score=4000,package_money=100)
print(total)
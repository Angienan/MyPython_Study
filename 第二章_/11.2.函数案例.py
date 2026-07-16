# def triangle_area(side,height):
#     """
#     计算三角形的面积
#     :param side: 三角形的低
#     :param height: 三角形的高
#     :return: 返回三角形的面积
#     """
#     return side * height / 2
# print(triangle_area(10,5))
#
# def count_aeiou(s):
#     """
#     统计字符串中元音字母的个数
#     :param s: 字符串
#     :return: 返回元音字符串的个数
#     """
#     num = 0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num += 1
#     return num
#
# print(count_aeiou('fiouioqjkldnkdnbvhgfis'))
#
# def calc_score(score_list):
#     """
#     计算成绩的最高分,最低分,平均分
#     :param score_list: 传入的成绩列表
#     :return: 返回成绩最高分,最低分,平均分
#     """
#     max_score =max(score_list)
#     min_score = min(score_list)
#     avg_score = round(sum(score_list) / len(score_list), 1)
#     return max_score, min_score, avg_score
#
# s_list = [134,35,24,65,76,98,34]
# max_score, min_score, avg_score = calc_score(s_list)
# print(max_score, min_score, avg_score)
#
#案例1
# def count_grade(score):
#     """
#     根据传入的分数,计算对应的分数等级并返回
#     :param score: 传入的分数
#     :return: 返回等级"A,B,C,D"
#     """
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     elif score >= 70:
#         return 'C'
#     else:
#         return 'D'
# print(count_grade(40))

#案例2
# def check_for_palindrome(s):
#     """
#     判断一个字符串是否是回文
#     :param s: 传入的字符串
#     :return: 返回bool值
#     """
#     if s == s[::-1]:
#         return True
#     else:
#         return False
#
# print(check_for_palindrome("12333321"))


# #案例3
# def time_conversion(seconds):
#     """
#     根据输入的秒数完成时间的转换
#     :param seconds: 输入的秒数
#     :return: 返回小时,分钟,秒
#     """
#     if seconds < 0 :
#         print("输入的秒数不能为负数")
#     hour = seconds //3600
#     remain = seconds % 3600
#     minute = remain // 60
#     second = remain % 60
#
#     return f"{hour:02d}:{minute:02d}:{second:02d}"
#
# print(time_conversion(5406))

#案例4
# def determine_triangle(a,b,c):
#     """
#     判断三角形的具体形状
#     :param a: 三角形的边
#     :param b: 三角形的边
#     :param c: 三角形的边
#     :return: 返回等腰三角形或等边三角形或普通三角形或不是三角形
#     """
#     if a+b>c and a+c>b and b+c>a:
#         if a==b==c:
#             return "可以构成等边三角形"
#         elif a==b or b==c or a==c:
#             return "可以构成等腰三角形"
#         else:
#             return "可以构成普通三角形"
#     else:
#         return "不能构成三角形"
#
# print(determine_triangle(2,2,3))
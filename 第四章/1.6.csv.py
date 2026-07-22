"""
csv: comma-separated values,逗号分隔值,是一种简单的,通用的文本文件格式,用于存储表格数据,可以直接用Excel打开
"""
import csv

# with open("csv.data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,性别,年龄,爱好\n")
#     f.write("张三,男,25,篮球\n")
#     f.write("李四,女,22,阅读\n")
#     f.write("王五,男,28,游泳\n")
# """
# 姓名,性别,年龄,爱好
# 张三,男,25,篮球
# 李四,女,22,阅读
# 王五,男,28,游泳
# 赵六,女,30,绘画
# 孙七,男,24,音乐
#
# """
# with open("csv.data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

with open("csv.data/02.csv","w",encoding="utf-8",newline="") as f:
     writer= csv.DictWriter(f,fieldnames=["姓名","性别","年龄","爱好"])
     writer.writeheader()
     writer.writerow({"姓名":"张三","性别":"男","年龄":25,"爱好":"篮球"})
     writer.writerow({"姓名":"张三","性别":"男","年龄":25,"爱好":"篮球"})
     writer.writerow({"姓名":"张三","性别":"男","年龄":25,"爱好":"篮球"})
with open("csv.data/02.csv","r",encoding="utf-8",newline="") as f:
     reader = csv.DictReader(f)
     for row in reader:
          print(row)
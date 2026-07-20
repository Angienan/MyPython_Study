"""
文件入门,基本分为三步,打开,读写,关闭
编码:将字符转换为可以为计算机存储和处理的数字代码的规则系统

文件操作的三步:
打开:open
读/写:read(),write()
关闭:close()

"""
from idlelib.iomenu import encoding

# f=open("D:\\Programming\\Python\\Python_Code\\MyPython_Study\\第三章\\AI应用\\resources\望庐山瀑布.txt", "r", encoding="utf-8")

# content=f.read()
# print(content)
# content = f.readlines()
# for line in content:
#     print(line.strip())
#
# f.close()

#
# f=open("D:\\Programming\\Python\\Python_Code\\MyPython_Study\\第三章\\AI应用\\resources\\静夜思.txt", "w", encoding="utf-8")
# try:
#     f.write("静夜思(李白)\n\n")
#     f.write("床前明月光\n")
#     f.write("疑是地上霜\n")
#     i=1/0
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
# finally:
#     print("正常关闭")
#     f.close()

"""with语句,上下文管理器,作文是确保资源总是被正确获取和释放,也是项目开发中推荐的方式"""
with open("AI应用/resources/静夜思.txt", "w", encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")

    f.write("举头望明月\n")
    f.write("低头思故乡\n")

"""
相对路径:相对于当前文件的路径   "resources/静夜思"   .:当前目录---> ./resources/望庐山.txt   ./可以省略
                                               ..:上一级目录
绝对路径:从根目录开始的路径  "D:\\Programming\\Python\\Python_Code\\MyPython_Study\\第三章\\AI应用\\resources\\静夜思.txt"

r: 只读
w:只写
a:追加
"""

# while 语法结构
i = 1
while i<=10:
    print(i)
    i+=1
else:
    print("执行完毕")

# 案例1
total = 0
num = 1

while num <= 100:
    if num % 2 == 0:
        total += num
    num+=1

print(total)
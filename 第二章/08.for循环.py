msg = "hello-world"

for i in msg:
    print(i)
else:
    print("循环结束")


total = 0
for i in range(1,101,2):
    total += i
print(f"循环结束,{total}")



total2 = 0
for i in range(100,501):
    if i % 3 == 0:
        total2 += i
print(f"循环结束{total2}")
# range语句 : 生成制定规则的数字序列

range(5)
range(1,10)
range(1,20,2)
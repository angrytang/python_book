num = int(input("需要输出多少个斐波那契数列："))

a1 = 0
a2 = 1
if num <= 2:
    print("请重新输入")
else:
    for i in range(num):
        a1, a2 = a2, a1 + a2
        print(a1, end=' ')
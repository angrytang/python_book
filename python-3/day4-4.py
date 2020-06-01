from math import sqrt

num = int(input("请输入需要校验的正整数："))
k = int(sqrt(num))
is_prime = True

for i in range(2, k+1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num >= 2:
    print("您输入的是素数")
else:
    print("您输入的不是素数")
"""
输出10000以内所有的完美数
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
"""
import math
"""
for num in range(1,10000):
    a = 0
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            a += i
    if num == a:
        print(num, end=' ')
"""
for num in range(1, 10000):
    result= 0
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            result +=  i
            if i > 1 and num // i != i:
                result += num // i
    if result == num:
        print(num, end=' ')
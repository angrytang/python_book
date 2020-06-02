"""
正整数的反转
"""

num = int(input('num = '))

a = 0
while num > 0:
    a = a * 10 + num % 10
    num //= 10

print("a = ",a)
"""
判断输入的边长能否构成三角形，能则计算出三角形的周长和面积
"""

print("请输入三角形的三条边长")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print("周长为: %f"%(a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f'%(area))
else:
    print('不能构成三角形')

def max2(x):
    m1, m2 = (x[0], x[1])if x[0]>x[1] else (x[1], x[0])
    for i in range(2, len(x)):
        if x[i] > m1:
            m2 = m1
            m1 = x[i]
        elif x[i] > m2:
            m2 = x[i]
    return m1, m2

if __name__ == '__main__':
    x = (1, 2, 3, 4, 5, 6)
    print(max2(x))
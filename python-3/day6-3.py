def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add())
print(add(1))
print(add(1, 3, 5))

a = (1, 2, 3, 5)
print(add(a))
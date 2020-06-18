set1 = {1, 2, 3, 3, 3, 2}
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))

set1.add(4)
print(set1)

set2.update([11, 12])
set2.discard(5)
print(set2)

print(set3)
print(set3.pop())
print(set3)
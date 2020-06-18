scores = {'骆昊':95, '白元芳':78, '狄仁杰':82}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
items2 = dict(zip(['a', 'b', 'c'], '123'))
items3 = {num:num ** 2 for num in range(1, 19)}
print(items1, items2, items3)

print(scores['骆昊'])
print(scores['狄仁杰'])

for key in scores:
    print(key,':',scores[key])

scores['白元芳'] = 65
scores['诸葛王朗'] = 74
scores.update(冷面=67, 方启鹤=85)


print(scores.get('武则天'))
print(scores.get('武则天', 60))
if '武则天' in scores:
    print(scores['武则天'])
print(scores)

print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
scores.clear()
print(scores)


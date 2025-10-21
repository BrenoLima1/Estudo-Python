from itertools import count

c1 = count(8, 8)
r1 = range(8, 100, 8)

print('Count:')
for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('Range:')
for i in r1:
    print(i)

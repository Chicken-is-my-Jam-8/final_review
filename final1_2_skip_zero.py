
a = [1, 2, 0, 3]
b = [3, 4, 6, 5]
total = 0
for x in range(len(a)):
    if a[x] == 0 or b[x] == 0:
        continue
    total += (a[x] * b[x])
print(a)
print(b)
print(total)'

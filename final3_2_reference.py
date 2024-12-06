
#this will append 4 to x because using the = operator with list only creates a reference to the original, not a copy
x = [1, 2, 3]
y = x
y.append(4)
print(x)

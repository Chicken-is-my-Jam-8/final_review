
text = "Python 3.9 is great for 2024!"
t_string = ''
for x in text:
    if x.isdigit() == True:
        continue
    t_string = t_string + x
print(text)
text = t_string
print(text)


sentence = "Chicago is very different from Boston"
print(sentence)
sentence = sentence.split()
length = 0
position = 0
for x in sentence:
    if len(x) <= length:
        continue
    length = len(x)
print("The longest words in this sentence are:")
for x in sentence:
    if len(x) == length:
        print(x)

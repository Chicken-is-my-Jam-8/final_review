
text = "Hello World! Python3"
digits = 0
letters = 0
capital_letters = 0
for x in text:
    if x.isdigit() == True:
        digits += 1
    if x.islower() == True:
        letters += 1
    if x.isupper() == True:
        capital_letters += 1
print(text)
print(f"digits: {digits}")
print(f"letters: {letters}")
print(f"capital letters: {capital_letters}")

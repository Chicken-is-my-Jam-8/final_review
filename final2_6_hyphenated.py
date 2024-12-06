
words = ["Deep", "fried", "wings"]
#print(words[0] + "-" + words[1] + "-" + words[2])
new_string = ""
for x in words:
	new_string = new_string + x + "-"
new_string = new_string.rstrip("-")
print(new_string)

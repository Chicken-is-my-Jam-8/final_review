
text = ['line1 ', 'line2 ', 'line3 ']
new_string = ''
for x in text:
	new_string = new_string + x + "\n"
new_string = new_string.rstrip("\n")
print(new_string)


pal1 = input("Please enter a string: ")
pal2 = input("Please enter another string: ")
r_pal = ''
for x in range(1, (len(pal1) + 1)):
	r_pal = r_pal + pal1[-x]
if pal2 == r_pal:
	print("These are palindromes")
else:
	print("These are not palindromes")

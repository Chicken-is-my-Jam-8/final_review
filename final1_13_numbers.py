
try:
	# Promp user for file name
	file_name = input("enter the:name of the file containing numbers: ")
	total = 0 # To store the sum of numbers

	# Open and process the file
	with open(file_name, 'r') as file:
		for line in file:
			try:
				# Try to conver the line to a number
				number = float(line.strip()) #Use strip() to remove extra whitespace
				total += number
			except ValueError:
				print(f"Invalid data found: '{line.strip()}'. Skippin this line.")
	print(f"the total sum of numbers in the file is: {total}")

except FileNotFoundError:
	print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
	print(f"Error: Permission deneied to read the file '{file_name}'")
except Exception as e:
	print(f"An unexcepted error occurred: {e}'")

# will print exception message for the line containing "abc"
# next it will print the total of the numbers in numbers.txt

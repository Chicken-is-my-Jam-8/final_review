
total = 0
try:
	# Prompt user for file name
	file_name = input("Enter the name of the file to read: ")

	# Open and read the file
	with open(file_name, 'r') as file:
		for line in file:
			number = float(line.strip())
			#Use strip() to remove extra whitespace
			total += number
	print(f"The total sum of numbers in the file is: {total}")
except FileNotFoundError:
	print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
	print(f"Error: Permission denied to read the file '{file_name}',")
except ValueError as e:
	print(f"an unexpected error occurred: {e}")


#will print the value error message with numbers.txt as input 

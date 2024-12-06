
#with, as, Exception as e
try:
	# Prompt user for file name
	file_name = input("Enter the name of the file to read: ")

	# Open and read the file
	with open(file_name, 'r') as file:
		lines = file.readlines()

	# Count the number of lines
	line_count = len(lines)
	print(f"The file '{file_name}' has {line_count} lines.")
except FileNotFoundError:
	print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
	print(f"Error: Permission denied to read the file '{file_name}',")
except Exception as e:
	print(f"an unexpected error occurred: {e}")


#will output that the file has 0 lines

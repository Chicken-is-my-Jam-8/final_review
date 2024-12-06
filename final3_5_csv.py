
import csv

def demonstrate_division(file_name):
	try:
		with open(file_name, 'r') as file:
			reader = csv.reader(file)
			for row in reader:
				try:
					result = int(row[0])/ int(row[1])
					print(f"Result of division: {result}")
				except Exception as e:
					print(f"{e}")
	except FileNotFoundError:
		print(f"Error: The file '{file_name}' does not exist.")
demonstrate_division("data.csv")
#it's going to output the division of the first two rows
#untill it get to a row with only one field full
#then it will output an exception message

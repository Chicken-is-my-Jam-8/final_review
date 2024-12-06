
weight = int(input("Please enter your weight(Kg): "))
height = float(input("Please enter your height(meters) :"))
# height in meters
bmi = weight / (height * height)
if bmi > 25:
	print("Your BMI exceeds 25")
	print("You're overweight")


def main():
	quiz = {
	("What is the capital of Italy?", "Rome"),
	("What is 50 + 250?", "300"),
	("What is the largest planet in our solar system?", "Jupiter"),
	("Who wrote 'A thousand splendid sun'?", "Khaled Hosseini"),
	("What is the chemical symbol for water?", "H2O")}

	total_score = start_quiz(quiz)
	print(f"Your final score is {total_score} out of {len(quiz)}.")

def start_quiz(q):
	answer = ''
	total = 0
	for x in q:
		answer = input(f"{x[0]}: ")
		if answer == x[1]:
			print("Correct!")
			total += 1
		else:
			print("wrong")
	return total
		
main()

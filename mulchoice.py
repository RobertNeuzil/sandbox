class Multiple_Choice:
	def __init__(self, question, correctanswer, answer2, answer3, answer4):
		self.question = question
		self.correctanswer = correctanswer
		self.answer2 = answer2
		self.answer3 = answer3
		self.answer4 = answer4

one = Multiple_Choice("What color is the sky? ", "blue", "red", "green", "yellow")
two = Multiple_Choice("What color is the sun? ", "yellow", "red", "green", "blue")
three = Multiple_Choice("What color is the grass? ", "green", "yellow", "red", "blue") 

def run_test(one, two, three):
	score = 0
	print (one.question + "\n" + "\n" + one.correctanswer + "\n" + one.answer2 + "\n" + one.answer3 + "\n" + one.answer4 + "\n")
	user_answer = input("type answer here: ")
	print (two.question + "\n" + "\n" + two.correctanswer + "\n" + two.answer2 + "\n" + two.answer3 + "\n" + two.answer4 + "\n")
	user_answer_two = input("type answer here: ")
	print (three.question + "\n" + "\n" + three.correctanswer + "\n" + three.answer2 + "\n" + three.answer3 + "\n" + three.answer4 + "\n")
	user_answer_three = input("type answer here: ")

	if user_answer == one.correctanswer:
		score += 1

	else:
		pass

	if user_answer_two == two.correctanswer:
		score += 1
	else:
		pass

	if user_answer_three == three.correctanswer:
		score += 1
	else:
		pass

	print ("You got " + str(score) + " answers correct!")

run_test(one, two, three)


import random

def play_the_game():
	goal = random.randrange(1, 10)
	
	count = 0
	count +=1
	print ("Please guess a number between 1 and 10. You get 5 attempts")
	while count <= 5:
		user_guess = int(input("Please enter your guess here  "))
		if user_guess == goal:
			print (f"Congratulations! You correctly guessed {goal} as the number.")
			break
		else:
			print (f"Please try again {user_guess} was not correct")
			count +=1
	else:
		print (f"You have run out of guesses, the number was {goal}")
play_the_game()

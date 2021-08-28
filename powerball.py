#In order to win the lucky jackpot, powerball players must match five numbers between 1 and 69
#Plus an additional powerball number between one and 26
#Plays can either choose their own numbers or elect a "quick pick" that randomly generates the values for them
#This program creates a quick pick Powerball ticket for Powerball players
#The odds of winning a powerball jackpot are 1 in 292,201,338, the total possible combinations of the five white balls (1-69) and the separate red ball (1-26)
#An American Citizen is statistically more likely to become president than to win the Powerball, or they would be, under the assumption that politics isn't rigged.

import random as r
# We want to append the numbers in sequential order and choose another if there is a duplicate value, like choosing the number 11 twice. But we also don't want to throw out the red
#ball if it duplicates a white ball, as the game allows for that


def generate():
	white_sequential_order = set()
	full_numbers = []
#70 is the stopping parameter, numbers less than it are generated. We want to include 69. Same concept for red ball.
	white_ball = r.randrange(1,70)
	white_ball_two = r.randrange(1,70)
	white_ball_three = r.randrange(1,70)
	white_ball_four = r.randrange(1,70)
	white_ball_five = r.randrange(1,70)
	red_ball = r.randrange(1,27)
	white_sequential_order.add(white_ball)
	white_sequential_order.add(white_ball_two)
	white_sequential_order.add(white_ball_three)
	white_sequential_order.add(white_ball_four)
	white_sequential_order.add(white_ball_five)
	if len(white_sequential_order) == 5:
		print (f'Your white numbers are: {sorted(white_sequential_order)} and your red ball is {red_ball}')
	else:
	#When we find duplicates in the white numbers, we run the algorithim again until all values are unique
		generate()

generate()
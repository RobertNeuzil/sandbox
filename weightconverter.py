
def GetWeight():
	weight_number = int(input("What is your weight?: "))
	unit = input("Is this in P(pounds) or K(kilograms) ")

	if unit == "p" or unit == "P":
		print(f"You weigh {weight_number * 0.453592} Kilograms")
	elif unit == "K" or unit == "k":
		print (f"You weight {weight_number/0.453592} pounds") 
	else:
		print ("""
		Please try again
		""")
		GetWeight()


GetWeight()
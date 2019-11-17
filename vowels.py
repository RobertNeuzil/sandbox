'''
Are there any vowels in my string?

'''

my_string = "alex"
my_string = my_string.upper()
my_list = set(my_string)

def any_vowels(my_list):
	index = 0
	while index < len(my_list):
		for x in my_list:
			if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
				print (x + " is a vowel and was found in your list.")
				index += 1
				return True

			elif x != "A" or x != "E" or x != "I" or x != "O" or x != "U":
				index += 1
				return True
				
			if x != "A" or x != "E" or x != "I" or x != "O" or x != "U" and len(my_list) >= index:
				print ("There were no vowels found in the list")

				return False	

any_vowels(my_list)

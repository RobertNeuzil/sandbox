import random
num_list = []
for p in range (0, 1000):
	num_list.append(random.randint(1, 100))
	num_list.sort()
	
print(num_list)

def run_project(first, second, target):
	while first <= len(num_list):
		if num_list[first] + num_list[second] == target:
			print ("The numbers are " + str(num_list[first]) + " and " + str(num_list[second]))
			break
		elif num_list[first] + num_list[second] != target and num_list[first] <= len(num_list) and num_list[second] <= len(num_list):
			first += 1
			second += 1
		else:
			print ("No Good")
			
			break


"""
Progressive Tax Rate
income cap      marginal tax rate
  ¤10,000           0.00 (0%)
  ¤30,000           0.10 (10%)
 ¤100,000           0.25 (25%)
    --              0.40 (40%)



"""

print (""""


_______Progressive Tax Rate Calculator_______""")

income_entered = int(input("Enter your income for the year: "))


#income_entered = 12000

def tax_calculate(income):

	if income < 10000:
		print (f"Your income tax is {income * 0}")
	elif income > 10000 and income < 30000:
		remainder = income - 10000
		print (f"Your income tax is {remainder * 0.10}")
	elif income > 10000 and income < 100000:
		remainder = 0
		second_remainder = 20000 * 0.10
		third_remainder = (income - 30000) * (0.25) + remainder + second_remainder
		print (f"Your income tax is {third_remainder}")
	else:
		remainder = 0
		second_remainder = 20000 * .10
		third_remainder = 70000 * .25
		final_tax = ((income - 100000) *.40) + remainder + second_remainder + third_remainder
		print (f"Your income tax is {final_tax}")

tax_calculate(income_entered)
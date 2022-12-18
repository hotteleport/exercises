import math
salary = input("Your month salary? ")
salary = float(salary)
tax = input("What is your percentage of TAX? ")
tax = float(tax)

tax = salary * (tax / 100)
tax = "Tax is {} $".format(round(tax, 2))

Earnings = salary - tax
Earnings = "Earnings is {} $".format(round(Earnings, 2))



print(Earnings)
print(tax)

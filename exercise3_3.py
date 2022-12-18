# ask info
workhours = input("How many workhours this week? ")
workhours = float(workhours)
salary = input("Your hourly salary? ")
salary = float(salary)
# calculations
if workhours > 40:
    overtime_hours = workhours - 40
    wage2 = salary * 40 + (overtime_hours * salary * 1.5)
    print(f"Your weekly wage: {wage2}".format(round(wage2, 2)))

else:
    wage1 = workhours * salary
    print(f"Your weekly wage: {wage1}".format(round(wage1, 2)))
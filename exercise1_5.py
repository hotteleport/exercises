from tabulate import tabulate
table = [["First name","Year of birth","Salary", "Tax percentage" ],["Matt","1970 ", "2000", "22.8"],
          ["Maria","1980","2500","27.7" ],["Bob ","1990","1000", "19.7"]]
print(tabulate(table))

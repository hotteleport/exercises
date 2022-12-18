from functions import *
# ask data
data = input("Write all participants, seperated by a comma:\n")
# split data
data = data.split(",")
# list
show_numbered_list("Original order", data)
data.sort()
show_numbered_list("Alphabetic order by first name", data)
# make a structure
data.sort(key=lambda x: x.split()[-1])
for i in range(len(data)):
    data[i] = ' '.join(reversed(data[i].split(' ')))
# show list
show_numbered_list("Alphabetic order by last name", data)
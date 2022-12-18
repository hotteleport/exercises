import statistics
# ask a number of students
ask = input("How many students?\n ")
ask = int(ask)
score = 0
list_1 = list()
# ask score in the loop
for ask in range(ask):
    score = input("What is the grade?\n ")
    score = float(score)
    list_1.append(score)
# calculate average
average = sum(list_1) / len(list_1)
average = round(average, 2)
print(f"Average is {average}")
median = statistics.median(list_1)
print(f"Median is {median}")
biggest = max(list_1)
print(f"Max is {biggest}")
# add text description
if 0 <= average < 1:
    print("Bad result")
elif 1 <= average < 2:
    print("Weak result")
elif 2 <= average < 3:
    print("Average result")
elif 3 <= average < 4:
    print("Good result")
elif 4 <= average <= 5:
    print("Excellent result")
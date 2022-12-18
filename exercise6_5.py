# add products list
products = ["T1565_2020","T2432_2019",
"T8551_2018","T3345_2019",
"Y51372_2019", "Y76715_2017",
"E98144_2018", "T7733_2020",
"E7614_2021","Y82018_2020",
"E9722_2017","T61287_2021",
"E9152_2019","T7749_2021"]
# ask the order code from user
ordercode_from_user = input("What is the order code? ")
# use the split () -function in loop
for parts in products:
    parts = parts.split("_")
    if ordercode_from_user == parts[0]:
        print(f"Year of the order code: {parts[1]}")
    # if input info is not a year
    else:
        pass

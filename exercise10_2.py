# ask
read_or_write = input("Would you like to read or write into the guestbook? (r/w)\n")
# read
if read_or_write == "r":
    file = open("guestbook.txt", "r")
    data = file.read()
    list0 = data.split(" ")
    # print
    for info in data:
        print(info)
    file.close()
# write
elif read_or_write == "w":
    text = input("Add some text: ")
    file = open("guestbook.txt", "a", encoding="utf-8")
    file.write(text + " ")
    file.close()
 # 1 ex
def show_personal_info():
    print("John Williams!")
    print("Rovaniemi")
    print("Software Engineer")

 # 2 ex
def count_seconds(hours, minutes, seconds):
     result = hours * 3600 + minutes * 60 + seconds
     return result

 # 3 ex
def magazine_serial_check(serial):
    okay = True
    if len(serial) !=8:
        okay = False
    return okay
 # 4 ex
def show_numbered_list(title, data):
    print()
    print(title,": ")
    for i in range(len(data)):
         print(i + 1, ".", data[i])

 # 5 ex
def box_volume(width, height, depth):
    formula1 = width * height * depth
    return formula1
def ball_volume(radius):
    formula2 = (4 * 3.14 * radius ** 3) / 3
    return formula2
def pipe_volume(radius2, length):
    formula3 = 3.14 * radius2 ** 2 * length
    return formula3




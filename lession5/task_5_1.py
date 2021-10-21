my_file = open("m_file.txt", "w")
while 1:
    my_str = input("Введите строку:")
    if my_str == "":
        break
    else:
        my_file.writelines([my_str, "\n"])
my_file.close()


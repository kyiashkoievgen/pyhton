my_file = open('m.file_5.txt', "w")
my_file.write("23 46 786 23 356 8 56 234 46 86 975 64 523 3 4 35 547 68 67 4 53 5423 4 35 4 6 57 56 78 567 4 563"
              " 54 234 2 4 456 4")
my_file.close()
my_file = open('m.file_5.txt', "r")
my_file.close()
my_str = my_file.readline().split(" ")
sum_num = 0
for num in my_str:
    sum_num = sum_num + float(num)
print(sum_num)


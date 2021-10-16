my_file = open("m_file2.txt", "r")
i = 0
while 1:
    line = my_file.readline()
    if line == "":
        break
    words = line[:-1].split(" ")
    j = 0
    for w in words:
        if w != '':
            j = j+1
    print("строка %d слов %d" % (i, j))
    i = i + 1
print("в файле %d строк" % i)
my_file.close()
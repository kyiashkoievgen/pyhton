my_file = open("m_file3.txt", "r")
while 1:
    line = my_file.readline()
    if line == '':
        break
    worker = line.split(" ")
    if float(worker[1][:-1]) < 20000:
        print(worker[0])
my_file.close()
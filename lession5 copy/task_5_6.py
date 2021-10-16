import re
my_file = open("m_file6.txt", "r")
res_dic = dict()
while 1:
    line = my_file.readline()
    if line == '':
        break
    less = line.split(" ")
    res_sum = 0
    for item in less:
        match = re.search(r'\d*', item)
        if match and match[0] != "":
            res_sum = res_sum + int(match[0])
    res_dic.setdefault(less[0], res_sum)
print(res_dic)
my_file.close()

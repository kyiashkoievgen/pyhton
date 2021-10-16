import json
my_file = open("m_file7.txt", "r")
sum_profit = 0
i = 0
res_list = list()
dict_firm = dict()
dict_profit = dict()
while 1:
    line = my_file.readline()
    if line == "":
        break
    my_list = line[:-1].split(" ")
    profit = int(my_list[2])-int(my_list[3])
    dict_firm.setdefault(my_list[0], profit)
    if profit > 0:
        sum_profit = sum_profit + profit
        i = i + 1
avr_prof = sum_profit / i
dict_profit.setdefault("avr_profit", avr_prof)
res_list.append(dict_firm)
res_list.append(dict_profit)
with open("my_file.json", "w") as write_f:
    json.dump(res_list, write_f)

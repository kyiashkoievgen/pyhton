from itertools import count, cycle
start = 3
stop = 10
my_list = [12, 34, 56, 756, 45, 236]
for i in count(start):
    if i > stop:
        break
    else:
        print(i)
i = 1
for el in cycle(my_list):
    if i > stop:
        break
    print(el)
    i = i+1


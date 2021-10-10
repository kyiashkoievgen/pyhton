my_dict = dict()
for el in (2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11):
    i = my_dict.get(el)
    if i == None:
        i = 1
    else:
        i = i + 1
    my_dict.update({el: i})


def generator():
    for elf in my_dict:
        result = my_dict.get(elf)
        if result == 1:
            yield elf


print(*generator())
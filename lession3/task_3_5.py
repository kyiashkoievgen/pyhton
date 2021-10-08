def my_func(inp):
    split_str = inp.split(" ")
    res = 0
    for el in split_str:
        for el_1 in el:
            if ord(el_1) > 59 or ord(el_1) < 47:
                tr = 0
            else:
                tr = 1
        if tr:
            res = res + int(el)
    return res


res_sum = 0
while 1:
    my_str = input("введите строку чисел через пробел, спец символ '#':")
    try:
        i = my_str.index("#")
        res_sum = res_sum + my_func(my_str[:i])
        print(res_sum)
        break
    except ValueError:
        res_sum = res_sum + my_func(my_str)
        print(res_sum)

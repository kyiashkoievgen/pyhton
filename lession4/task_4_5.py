from functools import reduce


def multi(prev_el, el):
    return prev_el*el


my_list = [el for el in range(100, 1001)]
print(my_list)
print(reduce(multi, my_list))


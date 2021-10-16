my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def my_generator():
    i = 0
    while i < len(my_list) - 1:
        i = i + 1
        if my_list[i-1] < my_list[i]:
            yield my_list[i]


print(list(my_generator()))

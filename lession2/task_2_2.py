my_list_str = input("введите список ")
len_list = len(my_list_str)
my_list = list(my_list_str)
i = 1
while i < len_list:
    my_list[i], my_list[i - 1] = my_list[i-1], my_list[i]
    i = i + 2
print(my_list)


def my_func(*args):
    arg_1 = sorted(args, reverse=1)
    return arg_1[0] + arg_1[1]


print(my_func(2, 9, 10))

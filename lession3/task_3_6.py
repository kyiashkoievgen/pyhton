def int_func(f_str):
    l_word = f_str.lower()
    f_let = l_word[0].upper()
    return "".join([f_let, l_word[1:]])


print(int_func(input("Введите слово маленькими буквами:")))
my_str = input("Введите слова маленькими буквами:")
list_my_str = my_str.split(" ")
res_str = ""
for word in list_my_str:
    res_str = res_str + int_func(word) + " "
print(res_str)

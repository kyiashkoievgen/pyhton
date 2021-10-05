i = 0
num_my_dict_list = list()
while i < 3:
    name = input('Название товара: ')
    price = input('Цена: ')
    pcs = input("Кол-во: ")
    unit = input('единицы: ')
    my_dict = dict(название=name, цена=price, колво=pcs, ед=unit)
    num_my_dict = [i, my_dict]
    num_my_dict_list.append(tuple(num_my_dict))
    i = i + 1
output_dict = dict()
for keys_dict in my_dict.keys():
    output_dict.setdefault(keys_dict)
    i = 0
    new_list = list()
    while i < 3:
        if new_list.count(num_my_dict_list[i][1][keys_dict]) == 0:
            new_list.append(num_my_dict_list[i][1][keys_dict])
        i = i + 1
    output_dict[keys_dict] = new_list
print(output_dict)


var_1 = 1
var_2 = 2
var_3 = "Вася"
print(var_1, var_2, var_3)
name = input("Как тебя зовут? ")
age = input("Сколько тебе '" + name + "' лет ")
print('Ты', name, 'молодец, что дожил до ', age, 'лет')
sec_total = int(input("Сколько секунд "+name+" ты проживешь на этом свете? "))
hour_left = sec_total // 3600
minute_left = sec_total // 60 - hour_left * 60
sec_left =1
sec_total - minute_left * 60 - hour_left * 3600
print('Тебе, %s осталось жить (чч:мм:сс) %d:%d:%d' % (name, hour_left, minute_left, sec_left))
numbers = int(input(name + " введи любое число "))
out = numbers + numbers * 11 + numbers * 111
print('%s смотри как я могу! %d' % (name, out))
n0 = numbers
n1 = numbers // 10
tmp_result = n0 - (n1 * 10)
result = tmp_result
while n0 != n1:
    n0 = n1
    n1 = n1 // 10
    tmp_result = n0 - (n1 * 10)
    if result < tmp_result:
        result = tmp_result
print("Максимальная введенная цифра это %d" % result)


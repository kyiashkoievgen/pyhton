my_mounts = ["Зима", "Весна", "Лето", "Осень", "Декабрь"]
n = int(input("Введите номер месяца 1-12 "))
if n == 12:
    n = 1
else:
    n = n
print(my_mounts[n // 3])


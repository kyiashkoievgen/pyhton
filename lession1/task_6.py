a = int(input("Введите а="))
b = int(input("Введите b="))
i = 1
while 1:
    print("%d-й день:%.2f" % (i, a))
    a = a + (a * 0.1)
    i = i + 1
    if a > b:
        print("%d-й день:%.2f" % (i, a))
        print("Ответ: на %d-й день спортцмен достиг результата не менее %.2f км." % (i, b))
        break


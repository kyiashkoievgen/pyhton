def fact(num):
    for i in range(num):
        yield i+1


n = int(input('Введите n:'))
print("%d!=" % n, end='')
fac = 1
s = ''
for el in fact(n):
    s = s + str(el) + "*"
    fac = fac * el
print("%s=%d" % (s[:-1], fac))

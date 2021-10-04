rating = [2, 5, 8, 4, 2, 6, 5]
while 1:
    rating_el = int(input("Введите элемент рейтинга:"))
    for i, el in reversed(list(enumerate(rating))):
        if el == rating_el:
            rating.insert(i + 1, rating_el)
            break
        if i == 0:
            rating.append(rating_el)
    print(rating)

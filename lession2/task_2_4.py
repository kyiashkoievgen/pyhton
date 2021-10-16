my_words = input("Введите слова разделенные пробелом: ")
words_list = my_words.split(" ")
for ind, words_list in enumerate(words_list):
    print(ind, words_list[0:10])


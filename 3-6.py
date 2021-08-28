def int_func(word):
    return word.title()


line = input('Введите строку: ')

res = []
for word in line.split():
    res.append(int_func(word))

print(' '.join(res))

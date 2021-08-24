s = input('Введите строку, разделенную пробелами ')

for ind, word in enumerate(s.split()):
    print(f'{ind + 1}) {word[:10]}')

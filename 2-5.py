my_list = [7, 5, 3, 3, 2]

print('Введите число для добавления в рейтинг, для окончания необходимо ввести "end"')
while True:
    el = input()
    if el == 'end':
        break
    el = int(el)
    i = 0
    while i < len(my_list) and my_list[i] >= el:
        i += 1
    my_list.insert(i, el)
    print(my_list)

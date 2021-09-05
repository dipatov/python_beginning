with open('file3.txt', 'r') as f:
    s, n = 0, 0
    print('Имеют оклад меньше 20 тыс:')
    for line in f:
        surname, money = line.split()
        money = float(money)
        if money < 20000:
            print(surname)
        s += money
        n += 1
    print(f'Средний оклад: {round(s / n, 2)}')

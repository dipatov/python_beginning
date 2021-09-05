with open('file5.txt', 'w') as f:
    f.write(input('Введите набор чисел, разделенных пробелом: '))

with open('file5.txt', 'r') as f:
    numbers = f.read().split()
    res = sum([int(num) for num in numbers])
    print('Сумма чисел:', res)

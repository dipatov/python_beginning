print('Калькулятор')

a = float(input('Введите первое целое число: '))
operation = input('Введите операцию: ')
b = float(input('Введите второе целое число: '))

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    print(a / b)
elif operation == '//':
    print(a // b)
elif operation == '%':
    print(a % b)
else:
    print('Невалидная операция:(')

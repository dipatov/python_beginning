def div(dividend, divider):
    try:
        dividend, divider = float(dividend), float(divider)
        return round(dividend / divider, 3)
    except ZeroDivisionError:
        return 'Деление на ноль'
    except ValueError:
        return 'Неверный тип данных'


dividend, divider = input('Введите делимое: '), input('Введите делитель: ')

print(f'{dividend} / {divider} = {div(dividend, divider)}')

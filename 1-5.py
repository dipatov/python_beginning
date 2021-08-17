tr = int(input('Выручка: '))
tc = int(input('Издержки: '))

if tr > tc:
    print(f'Прибыль: {tr - tc}')
    print(f'Рентабильность: {(tr - tc) * 100 / tc:.2f}%')
    employees = int(input('Число работников: '))
    print(f'Прибыль на сотрудника: {(tr - tc) / employees:.2f}')
elif tr < tc:
    print(f'Убыток: {tr - tc}')

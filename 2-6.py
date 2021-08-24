n = int(input('Введите число товаров: '))

goods = []
for i in range(n):
    el = {}
    el['Название'] = input('Введите название товара: ')
    el['Цена'] = int(input('Введите цену товара: '))
    el['Количество'] = int(input('Введите количество товара: '))
    el['Ед.'] = input('Введите единицы товара: ')
    goods.append((i + 1, el))
print('Список товаров:', goods)

analytics = {
    'Название': [],
    'Цена': [],
    'Количество': [],
    'Ед.': [],
}
for i in range(n):
    for key in analytics:
        if goods[i][1][key] not in analytics[key]:
            analytics[key].append(goods[i][1][key])
print('Аналитики о товарах:', analytics)

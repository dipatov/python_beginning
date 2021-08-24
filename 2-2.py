arr = []

print('Введите значение, для окончания вводы введите "end"')
while True:
    el = input()
    if el == 'end':
        break
    if el.isdigit():
        el = int(el)
    arr.append(el)
print(f'Введенные значения: {arr}')

for i in range(1, len(arr), 2):
    arr[i - 1], arr[i] = arr[i], arr[i - 1]

print(f'Список с обменными значениями: {arr}')

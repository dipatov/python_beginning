from itertools import count

it = count(5)
el = next(it)
while el <= 13:
    print(el)
    el = next(it)

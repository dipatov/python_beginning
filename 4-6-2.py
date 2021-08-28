from itertools import cycle

c = cycle([123, False, 'asdf'])

for i in range(15):
    print(next(c))

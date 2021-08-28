from functools import reduce

print(reduce(lambda el1, el2: el1 * el2, list(range(100, 1001, 2))))

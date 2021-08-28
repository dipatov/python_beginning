my_func = lambda a, b, c: max(a, b, c) + max(min(a, b), min(b, c), min(a, c))

print(my_func(2, 1, 2))

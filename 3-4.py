def my_func(x, y):
    return x ** y


def my_func_1(x, y):
    answ = 1
    if y < 0:
        x = 1 / x
        y = -y
    for i in range(y):
        answ *= x
    return answ


def my_func_2(x, y):
    """
    Возводит число x в степень y

    (int, int) -> float

    >>> my_func_2(2, -2)
    0.25
    """
    if y < 0:
        x = 1 / x
        y = -y
    if y == 0:
        return 1
    elif (-y) % 2 == 0:
        t = my_func_2(x, y // 2)
        return t * t
    else:
        return my_func_2(x, y - 1) * x


print(my_func(2, -11))
print(my_func_1(2, -11))
print(my_func_2(2, -11))

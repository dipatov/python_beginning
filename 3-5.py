def my_func():
    res = 0

    def inner_func(s):
        nonlocal res
        t_s = 0
        for n in s.split():
            if n == 'q':
                res += t_s
                print(res)
                return False
            else:
                t_s += int(n)
        res += t_s
        print(f'{t_s}({res})')
        return True

    return inner_func


find_sum = my_func()
while find_sum(input('Введите строку чисел, для завершения нужно ввести символ "q": ')):
    pass

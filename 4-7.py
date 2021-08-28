def fact(n):
    answ = 1
    for i in range(1, n + 1):
        answ *= i
        yield answ


n = int(input())
for el in fact(n):
    print(el)

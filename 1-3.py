n = int(input())

raz = 1
temp = n
while temp > 9:
    temp //= 10
    raz += 1

print(f'{3 * n + 2 * n * (10 ** raz) + n * (10 ** (raz * 2))}')

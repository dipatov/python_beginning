num = int(input())
answer = 0

while num > 0:
    dig = num % 10
    if dig > answer:
        answer = dig
    num //= 10

print(answer)

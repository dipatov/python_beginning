with open('file1.txt', 'w') as f:
    while True:
        s = input()
        if s == '':
            break
        f.write(s + '\n')

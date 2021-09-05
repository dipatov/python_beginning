with open('file1.txt', 'r') as f:
    lines = f.readlines()
    print(f'Кол-во строк: {len(lines)}')
    for i, line in enumerate(lines, 1):
        words = line.split()
        print(f"В строке {i}: {len(words)} слов")

subjects = {}

with open('file6.txt', 'r') as f:
    for line in f:
        words = line.split()
        name = words[0]
        amount = words[1:]
        subjects[name] = sum([int(num.split('(')[0]) for num in amount if num != '—'])

print(subjects)

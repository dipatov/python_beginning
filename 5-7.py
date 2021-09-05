import json

res = [{}, {'average_profit': 0}]
n = 0

with open('file7.txt', 'r') as f:
    for line in f:
        line = line.split()
        income = int(line[2]) - int(line[3])
        res[0][line[0]] = income
        if income >= 0:
            n += 1
            res[1]['average_profit'] += income

if n > 0:
    res[1]['average_profit'] /= n

with open('file7.json', 'w') as fj:
    json.dump(res, fj, indent=2, ensure_ascii=False)

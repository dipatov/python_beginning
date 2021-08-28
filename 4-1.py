from sys import argv

_, hours, money_per_hour, premium = argv
hours, money_per_hour, premium = int(hours), int(money_per_hour), int(premium)
print((hours * money_per_hour) + premium)

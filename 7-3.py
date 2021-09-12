class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            print('Отрицательное число клеток')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, row_number):
        cells = ['*' * row_number] * (self.number // row_number)
        if self.number % row_number != 0:
            cells.append('*' * (self.number % row_number))
        return '\n'.join(cells)


a = Cell(15)
b = Cell(4)
print((a + b).make_order(3))
print()
print((a - b).make_order(20))
print()
b - a
print((a * b).make_order(11))
print()
print((a / b).make_order(2))

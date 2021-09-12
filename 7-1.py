class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(lambda x: str(x), row)) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in
                           range(len(self.matrix))])
        else:
            raise IndexError


matrix = Matrix([[1, 20, 10], [3, 4, 11]])
matrix2 = Matrix([[1, 20, 5], [1, 3, 4]])

print(matrix)
print()
print(matrix + matrix2)

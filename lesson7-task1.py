class ShapeError(Exception):
    pass


class Matrix:

    def __init__(self, mat: list):
        self.mat = mat

    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in j]) for j in self.mat])

    def __add__(self, other):
        if other.shape != self.shape:
            raise ShapeError(f'Arguments must be same shape!. Got array with {other.shape} shape.')
        else:
            summa = [[i + j for i, j in zip(line1, line2)] for line1, line2 in zip(self.mat, other.mat)]
            return Matrix(summa)

    @property
    def shape(self):
        return len(self.mat), len(self.mat[0])


a = [[1, 2, 3],
     [4, 5, 6]]
# b = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]] # Выброс ShapeError

b = [[1, 2, 3],
     [4, 5, 6]]

matrA = Matrix(a)
matrB = Matrix(b)
matrC = matrA + matrB
print(f'Матрица A:\n{matrA}')
print(f'Матрица B:\n{matrB}')
print(f'Результат сложения:\n{matrC}')

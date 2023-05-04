class Matrix:
    def __init__(self, matrix_string):
        self.matrix = _decoder(matrix_string)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]


def _decoder(matrix_string):
    strings = [x.split(" ") for x in matrix_string.split("\n")]
    return [[int(element) for element in row] for row in strings]

print(Matrix("1").column(1))
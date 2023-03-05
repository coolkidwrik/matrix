
# Matrix is a mathematical matrix with similar calculable characteristics
# will be represented using a 2D array with dimensions n x m
class Matrix:

    @staticmethod
    def is_square(matrix):
        return len(matrix) == len(matrix[0])

    @staticmethod
    def dimensions(matrix):
        n = len(matrix)
        m = len(matrix[0])
        return n, m

    @staticmethod
    def determinant(mat):
        n, m = Matrix.dimensions(mat)
        if Matrix.is_square(mat):
            if n == 1:
                return mat[0][0]
            else:
                return Matrix.determinant(mat[1:n-1][1:m-1])
        else:
            raise Exception("Matrix is not square!")

    # constructor for a matrix
    # if no arguments, then creates an empty 2D tuple, else takes in a 2D tuple
    def __init__(self, *args):
        if len(args) == 0:
            self.mat = ()
        else:
            self.mat = args[0]

    def cofactor(self):
        pass

    def adjugate(self):
        pass

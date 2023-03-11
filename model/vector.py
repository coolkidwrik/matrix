class Vector:
    def __init__(self, *args: float):
        vector = []
        for i in range(len(args)):
            vector[i] = args[i]

        self.dimension = len(vector)
        self.vector = vector

    def __repr__(self):
        temp = "<"
        for i in self.vector[:-1]:
            temp = temp + i + ", "
        return temp + f", {self.vector[-1]}>"

    @staticmethod
    def dot(v1, v2):
        length = min(v1.dimension, v2.dimension)
        vec1 = v1.vector
        vec2 = v2.vector
        temp = 0
        for i in range(length):
            temp += vec1[i]*vec2[i]
        return temp

    # only applying to 3 dimensions(not 7)
    @staticmethod
    def cross(v1, v2):
        # assertions
        assert v1.dimension <= 3, f"first vector cannot be expressed in 3 dimensions"
        assert v2.dimension <= 3, f"second vector cannot be expressed in 3 dimensions"

        cross_product = []
        vector_less_than_3_correction(v1)
        vector_less_than_3_correction(v2)

        cross_product[0] = v1[2]*v2[3] - v2[2]*v1[3]
        cross_product[1] = v2[1] * v1[3] - v1[1] * v2[3]
        cross_product[2] = v1[1] * v2[2] - v2[1] * v1[2]
        return cross_product


def vector_less_than_3_correction(v: Vector):
    if v.dimension < 3:
        for i in range(3):
            if i >= v.dimension:
                v[i] = 0

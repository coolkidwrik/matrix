import copy

class Vector:
    def __init__(self, *args):
        vector = []
        for i in range(len(args)):
            vector.append(args[i])

        self.dimension = len(vector)
        self.vector = vector

    def __repr__(self):
        temp = "<"
        for i in self.vector[:-1]:
            temp = temp + str(i) + ", "
        return temp + f"{self.vector[-1]}>"

    @staticmethod
    def scale(v, n: float):
        for i in range(v.dimension):
            v.vector[i] = v.vector[i]*n
        return v

    @staticmethod
    def add_vector(v1, v2):
        nv1 = copy.deepcopy(v1)
        nv2 = copy.deepcopy(v2)
        if v1.dimension < v2.dimension:
            nv1 = vector_correction(v1, v2.dimension)
        else:
            nv2 = vector_correction(v2, v1.dimension)
        for i in range(v1.dimension):
            nv1.vector[i] += nv2.vector[i]
        return nv1


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
        vf = copy.deepcopy(v1)
        v1 = vector_less_than_3_correction(v1).vector
        v2 = vector_less_than_3_correction(v2).vector

        cross_product.append(v1[1]*v2[2] - v2[1]*v1[2])
        cross_product.append(v2[0] * v1[2] - v1[0] * v2[2])
        cross_product.append(v1[0] * v2[1] - v2[0] * v1[1])
        vf.dimension = 3
        vf.vector = cross_product
        return vf


def vector_less_than_3_correction(v: Vector):
    return vector_correction(v, 3)


def vector_correction(v: Vector, n: float):
    v0 = copy.deepcopy(v)
    if v0.dimension < n:
        for i in range(n):
            if i >= v0.dimension:
                v0.vector.append(0)
                v0.dimension += 1
    return v0

import model.matrix as m
import model.vector as v

p0 = (1, 2, 3, 4, 5)

p1 = ((1, 2),
      (3, 4))

p2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

p3 = ((1, 2, 3, 4),
      (5, 6, 7, 8))

v1 = v.Vector(1, 2)
v2 = v.Vector(3, 2, 1)

print(v.Vector.dot(v1, v2))
print(v.Vector.cross(v1, v2))
print(v.Vector.scale(v1, 3))
print(v.Vector.add_vector(v1, v2))

print(v1)
print(v2)

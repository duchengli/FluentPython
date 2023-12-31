from math import hypot


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
v = Vector(3, 4)
print(v1)
print(v2)
print(abs(v1))
print(v * 3)
print(abs(v * 3))

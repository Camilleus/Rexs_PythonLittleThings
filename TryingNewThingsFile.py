class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x
        else:
            self.__x = None

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y
        else:
            self.__y = None

    def __str__(self):
        return f'Point({self.x},{self.y})'


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y

    def __str__(self):
        return f'Vector({self[0]},{self[1]})'

    def __call__(self, value=None):
        if value is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * value, self.coordinates.y * value)

    def __add__(self, vector):
        new_x = self.coordinates.x + vector.coordinates.x
        new_y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(new_x, new_y))

    def __sub__(self, vector):
        new_x = self.coordinates.x - vector.coordinates.x
        new_y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(new_x, new_y))


p = Point(5, 5)
print(p.x)

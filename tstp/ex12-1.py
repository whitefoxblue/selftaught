class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length


class Square:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side


rectangle = Rectangle(2, 4)
square = Square(4)

print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())

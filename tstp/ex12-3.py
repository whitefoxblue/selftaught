class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
#        self.shape = Shape()

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.length


class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return 4 * self.side


rectangle = Rectangle(5, 10)
square = Square(4)
#rectangle.shape.what_am_i()
rectangle.what_am_i()
square.what_am_i()




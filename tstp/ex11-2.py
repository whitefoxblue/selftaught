import math

class Circle():
#    def __init__(self, r):
#        self.radius = r

    def area(self, r):
        self.radius = r
#        area = math.pi * self.radius ** 2
        area = self.radius ** 2 * math.pi
        print(area)

#circle = Circle(3)
circle = Circle()

circle.area(3)

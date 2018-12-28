class Hexagon():
    def __init__(self, l):
        self.length = l

    def area(self):
        return 6 * self.length

hexagon = Hexagon(5)

print(hexagon.area())

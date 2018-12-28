class Square:
    def __init__(self, s):
        self.side = s
        
    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, v):
#        self.var = v
#        self.side = self.side + self.var
        self.side += v
        print("Side was =", self.side - v, "now =", self.side)

square = Square(4)
square.change_size(2)

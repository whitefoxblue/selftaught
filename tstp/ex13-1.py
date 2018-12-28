class Square():
    square_list = []

    def __init__(self, s1):
        self.side1 = s1
        self.square_list.append(self)

    def area(self):
        area = side1 * 4

square1 = Square(4)
square2 = Square(6)
square3 = Square(13)

print(Square.square_list)

print(Square.square_list[0].side1)
    

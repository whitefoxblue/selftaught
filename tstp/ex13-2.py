class Shape():
    def what_am_i(self):
        print("I am a shape.")
        
class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.side1 = s1
        self.square_list.append(self)

    def calc_peri(self):
        area = side1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side1, self.side1, self.side1, self.side1)
#        return (str(self.side1) +
#               " by " +
#               str(self.side1) +
#               " by " +
#               str(self.side1) +
#               " by " +
#               str(self.side1))
    

print(Square(29))


    




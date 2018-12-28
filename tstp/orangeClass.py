class Orange():
    def __init__(self, w, c):
        """weights are in oz"""
        self.weight = w
        self.color = c
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

#or1 = Orange(10, "dark orange")
#or1.weight = 100
#or1.color = "light orange"
#print(or1)
#print(or1.weight)
#print(or1.color)

#or1 = Orange(4, "light orange")
#or2 = Orange(8, "dark orange")
#or3 = Orange(14, "yellow")

orange = Orange(6, "orange")
#print(orange.mold)
orange.rot(10,98)
print(orange.mold)

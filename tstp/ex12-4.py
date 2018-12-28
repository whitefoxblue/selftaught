class Rider:
    def __init__(self, n):
        self.name = n

    def rider_is(self):
        print(self.name)

class Horse:
    def __init__(self, b, r):
        self.breed = b
        self.rider = r

    def breed_is(self):
        print(self.breed)

    def rider_is(self):
        print(self.rider)


sam = Rider("Sam")
charlie = Horse("Quarter Horse", sam)

print(charlie.rider.name)

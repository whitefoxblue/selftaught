class Apple():
    def __init__(self, c, s, f, w):
        self.color = c
        self.size = s
        self.freshness = f
        self.worms = w

apple = Apple("red", "big", "new", False)

print(apple.color)
print(apple.size)
print(apple.freshness)
print("Worms?", apple.worms)
    

class Point:

    def __init__(self, x, y):
        print(f"creating new point with coordinates {x} and {y}")
        self.x = x
        self.y = y


    def shift(self, x, y):
        self.x = self.x + x
        self.y = self.y + y


p = Point(10, 20)
print(p.x)
print(p.y)




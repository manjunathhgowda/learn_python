class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2, 3)
p2 = Point(4, 5)

# This will raise an error
print(p1 + p2)  

# With Operator Overloading (__add__)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2

print(result)  # 6,8
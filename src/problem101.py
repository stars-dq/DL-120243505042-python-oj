import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isTriangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


a1, b1, c1, a2, b2, c2 = map(float, input().split())
t1 = Triangle(a1, b1, c1)
t2 = Triangle(a2, b2, c2)

if t1.isTriangle() and t2.isTriangle():
    total_area = t1.getArea() + t2.getArea()
    print(total_area)
else:
    print("failure")
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isTriangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def getPerimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    a1, b1, c1, a2, b2, c2 = map(float, input().split())
    t1 = Triangle(a1, b1, c1)
    t2 = Triangle(a2, b2, c2)

    if t1.isTriangle() and t2.isTriangle():
        p = t1.getPerimeter() - t2.getPerimeter()
        if p.is_integer():
            p=int(p)
        print(p)
    else:
        print("failure")
    
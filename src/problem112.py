import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displayPoint(self):
        x_display = int(self.x) if self.x.is_integer() else self.x
        y_display = int(self.y) if self.y.is_integer() else self.y
        print(f"Point({x_display},{y_display})")


def calDistance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx ** 2 + dy ** 2)


if __name__ == "__main__":
    x1, y1, x2, y2 = map(float, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    p1.displayPoint()
    p2.displayPoint()

    distance = calDistance(p1, p2)
    print(f"Distance:{distance:.4f}")
    
class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def getArea(self):
        return 2 * 3.14 * self.r * (self.r + self.h)

    def getVolume(self):
        return 3.14 * self.r * self.r * self.h


if __name__ == "__main__":
    r, h = map(float, input().split())
    cylinder = Cylinder(r, h)
    area = cylinder.getArea()
    volume = cylinder.getVolume()
    print(f"{area} {volume}")
    
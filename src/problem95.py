class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def displayPoint(self):
        print(f"({self.x},{self.y})")
x,y=map(float,input().split())
if x.is_integer():
    x=int(x)
if y.is_integer():
    y=int(y)
p1=Point(x,y)
p1.displayPoint()

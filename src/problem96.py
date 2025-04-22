class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def setPoint(self,xx,yy):
        self.x=xx
        self.y=yy
    def displayPoint(self):
        print(f"({self.x},{self.y})")
x1,y1,x2,y2=map(float,input().split())
if x1.is_integer():
    x1=int(x1)
if y1.is_integer():
    y=int(y1)
if x2.is_integer():
    x2=int(x2)
if y2.is_integer():
    y2=int(y2)
p1=Point(x1,y1)
p1.displayPoint()
p1.setPoint(x2,y2)
p1.displayPoint()

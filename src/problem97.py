class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def setPoint(self,xx,yy):
        self.x=xx
        self.y=yy
    def leftMove(self,delta_x):
        self.x=self.x-delta_x
    def upMove(self,delta_y):
        self.y+=delta_y
    def displayPoint(self):
        print(f"({self.x},{self.y})")
x1,y1,dx,dy,x2,y2=map(float,input().split())
if x1.is_integer():
    x1=int(x1)
if y1.is_integer():
    y=int(y1)
if x2.is_integer():
    x2=int(x2)
if y2.is_integer():
    y2=int(y2)
if dx.is_integer():
    dx=int(dx)
if dy.is_integer():
    dy=int(dy)
p1=Point()
p1.displayPoint()
p1.setPoint(x1,y1)
p1.displayPoint()
p1.leftMove(dx)
p1.displayPoint()
p1.upMove(dy)
p1.displayPoint()
p2=Point(x2,y2)
p2.displayPoint()
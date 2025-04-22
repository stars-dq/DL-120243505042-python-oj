class Rectangle:
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
w,h=map(float,input().split())
if w.is_integer():
    w=int(w)
if h.is_integer():
    h=int(h)
r1=Rectangle()
print(r1.getArea())
r2=Rectangle(w,h)
print(r2.getArea())
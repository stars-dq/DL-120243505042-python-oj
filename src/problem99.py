class Rectangle:
    def __init__(self,width=10,height=10):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
    def expandN(self,n):
        self.width*=n
        self.height*=n
w,h,n=map(float,input().split())
if w.is_integer():
    w=int(w)
if h.is_integer():
    h=int(h)
if n.is_integer():
    n=int(n)
r1=Rectangle()
print(r1.getArea())
r2=Rectangle(w,h)
print(round(r2.getArea(),1))
r2.expandN(n)
print(round(r2.getArea(),1))
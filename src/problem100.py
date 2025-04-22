class Rectangle:
    def __init__(self,width=10,height=10):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
    def expandN(self,n):
        self.width*=n
        self.height*=n
w1,h1,w2,h2=map(float,input().split())
if w1.is_integer():
    w1=int(w1)
if h1.is_integer():
    h1=int(h1)
if w2.is_integer():
    w2=int(w2)
if h2.is_integer():
    h2=int(h2)
r1=Rectangle(w1,h1)
a1=r1.getArea()
r2=Rectangle(w2,h2)
a2=r2.getArea()
if a1>a2:
    print(f"{a1}>{a2}")
elif a2<a2:
    print(f"{a1}<{a2}")
else:
    print(f"{a1}={a2}")
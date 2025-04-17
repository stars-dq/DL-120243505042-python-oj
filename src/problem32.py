x=1000
while x>=1000 and x<=9999:
    n=x
    g=n%10
    n=n//10
    s=n%10
    n=n//10
    h=s*10+g
    if (h+n)**2==x:
        print(x,end=" ")
    x=x+1
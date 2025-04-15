n=100
while n>=100 and n<=999:
    x=n
    g=x%10
    x=x//10
    s=x%10
    x=x//10
    b=x
    if b**3+s**3+g**3==n:
        print(n,end=" ")
    n=n+1
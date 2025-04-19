def m(x,n):
    if n==0:
        return 1
    return x*m(x,n-1)
x,n=map(float,input().split())
print(round(m(x,n),3))
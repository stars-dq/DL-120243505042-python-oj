n=int(input())
d=0
while n>0:
    n=n-(n//2+2)
    d=d+1
print(d)
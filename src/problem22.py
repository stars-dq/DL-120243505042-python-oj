x=list(map(int,input().split()))
a=x[0]
i=0
while x[i]!=0:
    if x[i]>a:
       a=x[i]
    i=i+1
print(a)
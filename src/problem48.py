def ys(x):
    a=1
    n=0
    while a<=x:
        if x%a==0:
            n+=1
        a+=1
    return n
num=list(map(int,input().split()))
n=num[0]
count=0
for x in num[1:n+1]:
    count+=ys(x)
print(count)
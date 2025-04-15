x=list(map(int,input().split()))
i=0
n=0
while n<x[0]:
    i=i+1
    if x[i]>=60:
        print("Pass")
    else:
        print("Fail")
    n=n+1
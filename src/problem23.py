x=int(input())
b=2
while b<x:
    if x%b==0:
        break
    b=b+1
if b==x:
    print(1)
else:
    print(0)
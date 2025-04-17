n=int(input())
f1=1
f0=0
i=1
while i<n:
    f=f1+f0
    f0=f1
    f1=f
    i+=1
if f1 % 3 == 0:
        print("yes")
else:
        print("no")
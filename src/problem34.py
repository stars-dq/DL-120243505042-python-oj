num=int(input())
i=1
x=0
while i<=num:
    if num%i==0:
        x+=1
    i+=1
print(x)
n=int(input())
x=1
sum=0
while x<=n:
    sum=sum+1/(3*x-2)
    x=x+1
print(round(sum,5))
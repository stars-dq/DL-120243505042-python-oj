n,*strings=map(str,input().split())
n=int(n)
sum=0
for i in strings:
    sum+=len(i)
print(round(sum/n,5))
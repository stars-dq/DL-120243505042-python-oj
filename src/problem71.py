x=list(map(int,input().split()))
tem=x[0]
k=0
for i in x[:-1]:
    if i<tem:
        tem=i
for i in x:
    if i==tem:
        break
    k+=1
print(k)
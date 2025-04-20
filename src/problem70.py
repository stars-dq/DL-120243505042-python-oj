x=list(map(int,input().split()))
tem=x[0]
for i in x:
    if i>tem:
        tem=i
print(tem)
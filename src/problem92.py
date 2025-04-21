m,n=map(int,input().split())
jz=[]
for _ in range(m):
    row=list(map(int,input().split()))
    jz.append(row)
sum=0
for i in range(m):
    for k in range(n):
        if i==0 or i==m-1 or k==0 or k==n-1:
            sum+=jz[i][k]
print(sum)
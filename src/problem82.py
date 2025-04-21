n=int(input())
jz=[]
for _ in range(n):
    row=list(map(int,input().split()))
    jz.append(row)
sum=0
for i in range(n):
    for j in range(n):
        if i==j:
            sum+=jz[i][j]
        elif j+i==n-1:
            sum+=jz[i][j]
print(sum)
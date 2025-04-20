nums=list(map(int,input().split()))
n=nums[0]
x=nums[1:]
b=x[::-1]
i=0
y=[]
for i in range(n):
    if i%3==0:
        y.append(b[i])
print(" ".join(map(str,y)))
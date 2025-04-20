nums=list(map(int,input().split()))
n=nums[0]
x=nums[1:]
i=0
while i<n:
    if x[i]%3==0:
        print(x[i],end=" ")
    i+=1
print()
i=0
while i<n:
    if i%3==0:
        print(x[i],end=" ")
    i+=1

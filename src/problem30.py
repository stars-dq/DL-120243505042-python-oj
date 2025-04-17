sum= 0
i=0
num = list(map(int,input().split()))
while num[i] != 0:
    if num[i] % 2 != 0:
        sum+= num[i]
    i=i+1
print(sum)
def sushu(x):
    a=2
    while a<x:
        n=x%a
        if n==0:
            break
        a+=1
    if a==x:
        return 1
    else:
        return 0
nums = list(map(int, input().split()))
n = nums[0]
count = 0
for num in nums[1: n + 1]:
    if sushu(num):
        count += 1
print(count)
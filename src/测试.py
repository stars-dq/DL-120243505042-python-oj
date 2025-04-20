nums = list(map(int, input().split()))
n = nums[0]
x = nums[1:]

for i in range(n - 1, -1, -1):
    if x[i] % 3 == 0:
        print(x[i], end=" ")
print()

for i in range(n - 1, -1, -1):
    if i % 3 == 0:
        print(x[i], end=" ")
print()
data = list(map(int, input().split()))
x = 0
count = 0
while data[x] != 0:
    count += 1
    x += 1
nums = data[:x]
max_num = max(nums)
print(count, max_num)
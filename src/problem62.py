def f(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


nums = list(map(int, input().split()))
n = nums[0]
positive_sum = 0
positive_count = 0
for i in range(1, n + 1):
    num = nums[i]
    if f(num) == 1:
        positive_sum += num
        positive_count += 1

if positive_count == 0:
    average = 0
else:
    average = positive_sum / positive_count

print("{:.5f}".format(average))
    
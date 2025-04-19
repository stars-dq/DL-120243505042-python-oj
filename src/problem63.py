def digital_root(num):
    if num < 10:
        return num
    digit_sum = 0
    while num:
        digit_sum += num % 10
        num //= 10
    return digital_root(digit_sum)


nums = list(map(int, input().split()))
n = nums[0]
results = []
for i in range(1, n + 1):
    root = digital_root(nums[i])
    results.append(root)

print(" ".join(map(str, results)))
    
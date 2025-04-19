def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


nums = list(map(int, input().split()))[1:]
factorial_sum = 0
for num in nums:
    factorial_sum += fac(num)

average = factorial_sum / len(nums)
if average.is_integer():
    print(int(average))
else:
    print(average)
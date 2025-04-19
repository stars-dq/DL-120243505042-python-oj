def digit_sum(num):
    sum_value = 0
    while num:
        sum_value += num % 10
        num //= 10
    return sum_value


nums = list(map(int, input().split()))
result = []
for num in nums:
    if num == 0:
        break
    if digit_sum(num) % 2 != 0:
        result.append(num)

print(" ".join(map(str, result)))
    
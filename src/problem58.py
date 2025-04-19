def reverse_num(num):
    if num < 0:
        return -int(str(-num)[::-1])
    return int(str(num)[::-1])

nums = list(map(int, input().split()))
nums = [num for num in nums if num != 0]

sum_result = 0
for num in nums:
    reversed_num = reverse_num(num)
    sum_result += reversed_num

print(sum_result)
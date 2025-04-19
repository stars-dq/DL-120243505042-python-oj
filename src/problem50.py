def sum_of_odds(min_num, max_num):
    total = 0
    for num in range(min_num, max_num + 1):
        if num % 2 != 0:
            total = total + num
    return total


nums = list(map(int, input().split()))
n = nums[0]
max_sum = 0
for i in range(n):
    min_num = nums[2 * i + 1]
    max_num = nums[2 * i + 2]
    current_sum = sum_of_odds(min_num, max_num)
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
    
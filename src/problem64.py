def isodd(num):
    return num % 2 != 0


nums = list(map(int, input().split()))
odd_nums = []
for num in nums:
    if num == 0:
        break
    if isodd(num):
        odd_nums.append(num)

print(" ".join(map(str, odd_nums)), len(odd_nums))
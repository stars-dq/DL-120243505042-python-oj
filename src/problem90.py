def binary_to_decimal(binary_str):
    decimal_num = 0
    for digit in binary_str:
        decimal_num = decimal_num * 2 + int(digit)
    return decimal_num


n, *binary_nums = input().split()
n = int(n)
total_sum = 0
for binary_num in binary_nums:
    total_sum += binary_to_decimal(binary_num)

print(total_sum)
    
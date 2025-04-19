def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


nums = list(map(int, input().split()))
n = nums[0]
gcd_sum = 0
for i in range(n):
    num1 = nums[2 * i + 1]
    num2 = nums[2 * i + 2]
    current_gcd = gcd(num1, num2)
    gcd_sum += current_gcd

print(gcd_sum)
    
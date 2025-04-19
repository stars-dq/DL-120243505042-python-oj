def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


nums = list(map(int, input().split()))
n = nums[0]
lcm_sum = 0
for i in range(n):
    num1 = nums[2 * i + 1]
    num2 = nums[2 * i + 2]
    current_lcm = lcm(num1, num2)
    lcm_sum += current_lcm

print(lcm_sum)
    
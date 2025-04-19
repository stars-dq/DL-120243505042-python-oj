def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


min_num, max_num = map(int, input().split())
prime_sum = 0
for num in range(min_num, max_num + 1):
    if is_prime(num):
        prime_sum += num

print(prime_sum)
    
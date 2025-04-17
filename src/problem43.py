n = int(input())
prime_nums = []
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_nums.append(num)

for prime in prime_nums:
    print(prime, end=' ')
print()
print(len(prime_nums))
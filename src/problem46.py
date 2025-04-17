def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
numbers = list(map(int, input().split()))
max_prime = float('-inf')
for num in numbers:
    if num == 0:
        break
    if is_prime(num) and num > max_prime:
        max_prime = num
if max_prime == float('-inf'):
    print('no')
else:
    print(max_prime)
    
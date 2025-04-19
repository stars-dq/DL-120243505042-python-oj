def factor_sum(num):
    factor_sum_value = 0
    for i in range(1, num):
        if num % i == 0:
            factor_sum_value += i
    return factor_sum_value


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


m, n = map(int, input().split())

perfect_numbers = []
for i in range(1, n):
    if factor_sum(i) == i:
        perfect_numbers.append(i)
print(" ".join(map(str, perfect_numbers)))

prime_numbers = []
for i in range(m, n + 1):
    if is_prime(i):
        prime_numbers.append(i)
print(" ".join(map(str, prime_numbers)))
    
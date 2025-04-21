m, n = map(int, input().split())

is_prime = [1] * 100

is_prime[1] = 0


for i in range(2, 11):
    if is_prime[i]:
        for j in range(i * i, 100, i):
            is_prime[j] = 0

result = []
for i in range(m, n + 1):
    if is_prime[i]:
        result.append(i)

print(" ".join(map(str, result)))
    
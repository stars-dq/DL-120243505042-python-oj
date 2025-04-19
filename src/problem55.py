def power(n, k):
    return n ** k


n, k = map(int, input().split())
result = 0
for i in range(1, n + 1):
    result += power(i, k)

print(result)
    
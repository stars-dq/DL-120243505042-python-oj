def f(n):
    return sum(range(1, n + 1))


m, n = map(int, input().split())
result = f(m) + f(n)
print(result)
    
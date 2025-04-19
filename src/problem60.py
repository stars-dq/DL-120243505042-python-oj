def f(a, i):
    num = 0
    for _ in range(i):
        num = num * 10 + a
    return num


a, n = map(int, input().split())
total_sum = 0
for i in range(1, n + 1):
    total_sum += f(a, i)

print(total_sum)
    
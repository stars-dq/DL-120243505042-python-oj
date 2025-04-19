def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


e = float(input())
n = 1
term = 1
total_sum = 0
while term >= e:
    total_sum += term
    n += 1
    term = 1 / fibonacci(n)

print("{:.4f}".format(total_sum))
    
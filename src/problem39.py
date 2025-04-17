n = int(input())

while n >= 10:
    sum = 0
    temp = n
    while temp > 0:
        x = temp % 10
        sum += x
        temp = temp // 10
    n = sum

print(n)
    
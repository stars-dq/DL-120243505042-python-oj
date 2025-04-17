num = int(input())
sum = 0
while num > 0:
    x = num % 10
    if x % 2 == 0:
        sum += x
    num = num // 10

print(sum)
    
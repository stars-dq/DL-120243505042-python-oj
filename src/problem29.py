num = int(input())
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print(sum)
n, *numbers = map(int, input().split())
oddsum = 0
sum = 0

for num in numbers:
    if num % 2 == 0:
        sum += num ** 3
    else:
        oddsum += num ** 2

print(oddsum,sum)
    
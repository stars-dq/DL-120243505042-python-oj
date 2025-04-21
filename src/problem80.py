
numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)


x = int(input())


numbers = [i for i in numbers if i != x]


print(" ".join(map(str, numbers)))
    
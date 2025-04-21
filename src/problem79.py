
numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)
pos = int(input())


if 0 <= pos < len(numbers):
  
    del numbers[pos]
print(" ".join(map(str, numbers)))    
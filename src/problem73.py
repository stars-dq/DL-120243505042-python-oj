
input_str = input()
numbers = list(map(int, input_str.split()))

if 0 in numbers:
    zero_index = numbers.index(0)
    numbers = numbers[:zero_index]

numbers.sort()
n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print(median)
    
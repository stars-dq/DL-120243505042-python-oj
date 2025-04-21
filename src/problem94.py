def average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)
input_numbers = list(map(int, input().split()))
numbers = input_numbers[:input_numbers.index(0)]
a = average(numbers)
if a.is_integer():
    a=int(a)
print(a)
    
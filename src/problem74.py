def sort_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    for num in numbers:
        if num % 2 == 1:
            odd_numbers.append(num)
        else:
            even_numbers.append(num)
    odd_numbers.sort()
    even_numbers.sort()
    return odd_numbers + even_numbers


input_numbers=list(map(int,input().split()))
x=input_numbers[:-1]
sorted_numbers = sort_odd_even(x)
print(" ".join(map(str, sorted_numbers)))
    
n = int(input())
num = 2
while num <= n:
    sum_divisors = 1  
    i = 2
    while i <= int(num ** 0.5):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:  
                sum_divisors += num // i
        i += 1
    if sum_divisors == num:
        print(num, end=' ')
    num += 1
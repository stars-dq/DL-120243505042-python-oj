n = int(input())
fibonacci = [0] * n
if n > 0:
    fibonacci[0] = 0
if n > 1:
    fibonacci[1] = 1

for i in range(2, n):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

result = []
for num in fibonacci:
    if num % 3 == 2:
        result.append(num)

print(" ".join(map(str, result)))
    
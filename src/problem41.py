data = list(map(float, input().split()))
repeat = int(data[0])
results = []
index = 1
for _ in range(repeat):
    x = data[index]
    n = int(data[index + 1])
    power = x ** n
    if abs(power - round(power)) < 1e-9:
        power = int(round(power))
    else:
        power = round(power, 2)
    results.append(power)
    index += 2
print(" ".join(map(str, results)))
    
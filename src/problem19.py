hours = float(input())
if hours <= 10:
    cost = 30
elif hours <= 50:
    cost = hours * 3
else:
    cost = hours * 2.5
if cost.is_integer():
    cost=int(cost)
print(cost)
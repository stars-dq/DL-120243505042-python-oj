weight = float(input())
if weight <= 50:
    fee = weight * 0.15
else:
    fee = 50 * 0.15 + (weight - 50) * (0.15 + 0.10)
if fee.is_integer():
    fee=int(fee)
print(fee)
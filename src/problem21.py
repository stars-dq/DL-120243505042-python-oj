import math
a, b, c = map(float, input().split())
delta = b ** 2 - 4 * a * c
if delta > 0:
    root1 = (-b - math.sqrt(delta)) / (2 * a)
    root2 = (-b + math.sqrt(delta)) / (2 * a)
    if root1.is_integer():
        root1=int(root1)
    if root2.is_integer():
        root2=int(root2)
    print(min(root1, root2), max(root1, root2))
elif delta == 0:
    root = -b / (2 * a)
    if root.is_integer():
        root=int(root)
    print(root)
else:
    print("none")
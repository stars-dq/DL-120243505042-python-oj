input_str = input()
parts = input_str.split()
if len(parts) == 3:
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])
if a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")
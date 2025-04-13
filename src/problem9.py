str = input()
parts=str.split()
if len(parts)==3:
    a=parts[0]
    b=parts[1]
    c=parts[2]
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
    
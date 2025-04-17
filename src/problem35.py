m, n = map(int, input().split())
x=m
while n:
    tem=m%n
    m=n
    n=tem
print(m)
    
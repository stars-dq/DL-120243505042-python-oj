n, *m = map(int, input().split())
for i in m:
    if i <= 1000:
        print(0, end=' ')
    elif 1000 < i <= 3000:
        print(int(i * 0.03), end=' ')
    elif 3000 < i <= 5000:
        print(int(i * 0.04), end=' ')
    else:
        print(int(i * 0.06), end=' ')
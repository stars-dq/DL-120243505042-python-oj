n,*strings=map(str,input().split())
for i in strings:
    if i==i[::-1]:
        print(i,end=" ")
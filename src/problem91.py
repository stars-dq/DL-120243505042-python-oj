def move(sz):
    if len(sz)>3: 
        a=sz[-3:]
        b=sz[:-3]
        return a+b
    else:
        return sz
n,*p=input().split()
print(" ".join(move(p)))


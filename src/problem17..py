h,w=map(int,input().split())
s=h-110
if w>s+5:
    print("fat")
elif w<s-5:
    print("thin")
else:
    print("standard")
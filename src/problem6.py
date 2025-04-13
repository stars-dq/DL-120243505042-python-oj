x=int(input())
if x<=4:
    w=50
elif x<=8:
    w=50+(x-4)*20
else:
    w=50+4*20+(x-8)*30
print(w)
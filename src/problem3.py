x=float(input())
if x<=1000:
    s=0
elif x<=3000:
    s=x*.03
elif x<=5000:
    s=x*.04
else:
    s=x*.06
s = round(s, 2) 
if s.is_integer():
   s=int(s)
print(s)
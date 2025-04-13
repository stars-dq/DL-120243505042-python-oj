input_str = input()
parts = input_str.split()
if len(parts) == 2:
    y = int(parts[0])
    m = int(parts[1])
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print(31)
elif m==4 or m==6 or m==9 or m==11:
    print(30)
elif (y%400==0 or (y%4==0 and y%100!=0)) and m==2:
    print(29)
else:
    print(28)
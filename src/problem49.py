def fib(n):
    if n>=2:
        return fib(n-1)+fib(n-2)
    else:
        return n
min,max=map(int,input().split())
n=0
while fib(n)<max:
    if fib(n)>min:
        print(fib(n),end=" ")
    n+=1
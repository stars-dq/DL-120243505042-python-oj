def cow_count(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    return cow_count(n - 1) + cow_count(n - 3)

n = int(input())
print(cow_count(n))
    
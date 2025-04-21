m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
row = [0] * m
col = [0] * n
for i in range(m):
    row[i] = sum(matrix[i])
for j in range(n):
    for i in range(m):
        col[j] += matrix[i][j]
print("row:", end="")
for i in range(m):
    print(row[i], end=" ")
print()
print("col:", end="")
for j in range(n):
    print(col[j], end=" ")
print()
    
def insert_sorted(arr, x):
    index = 0
    while index < len(arr) and arr[index] > x:
        index += 1
    arr.insert(index, x)
    return arr


n, *numbers = map(int, input().split())
x = int(input())

# 从大到小排序
numbers.sort(reverse=True)

# 插入元素
result = insert_sorted(numbers, x)

# 输出结果
print(" ".join(map(str, result)))
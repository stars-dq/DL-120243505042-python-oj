def find_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


input_nums = list(map(int, input().split()))
x = input_nums.pop()
input_nums = input_nums[:input_nums.index(0)]
index = find_index(input_nums, x)
print(index)
    
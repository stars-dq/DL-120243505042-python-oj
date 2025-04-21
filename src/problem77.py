# 读取输入的整数，以 0 结束
numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

# 读取插入位置和插入元素
pos, x = map(int, input().split())

# 在指定位置插入元素
numbers.insert(pos, x)

# 输出插入后数组中的所有元素
print(" ".join(map(str, numbers)))    
# 获取输入
input_str = input()
# 将输入字符串按空格分割成列表
num_list = input_str.split()

total = 0
count = 0
index = 0

while True:
    num = int(num_list[index])
    if num == 0:
        break
    total += num
    count += 1
    index += 1

if count > 0:
    average = total / count
    print(average)

    
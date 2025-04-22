MaxSize = 100
class Array:
    def __init__(self):
        self.data = [0] * MaxSize
        self.length = 0
    def getLength(self):
        return self.length
    def insertX(self, i, x):
        if i < 0 or i > self.length or self.length >= MaxSize:
            raise ValueError("插入位置不合法或数组已满")
        for j in range(self.length, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.length += 1
    def displayArray(self):
        print(f"Length:{self.length}")
        print("Elements:", end="")
        for i in range(self.length):
            num = self.data[i]
            if num.is_integer():
                num = int(num)
            print(num, end=" " if i < self.length - 1 else "\n")
    def mySort(self):
        self.data[:self.length] = sorted(self.data[:self.length])

    def deleteAllX(self, x):
        count = 0
        new_length = 0
        for i in range(self.length):
            if self.data[i] != x:
                self.data[new_length] = self.data[i]
                new_length += 1
            else:
                count += 1
        self.length = new_length
        return count
if __name__ == "__main__":
    i = 0
    a = Array()
    inputs = list(map(float, input().split()))
    zero_index = inputs.index(0)
    for num in inputs[:zero_index]:
        try:
            a.insertX(i, num)
            i += 1
        except ValueError as e:
            print(e)
    a.displayArray()
    x = inputs[zero_index + 1]
    n = a.deleteAllX(x)
    print(f"Count of deleted elements:{n}")
    a.mySort()
    a.displayArray()
    
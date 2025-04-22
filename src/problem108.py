class Array:
    def __init__(self, size=100):
        self.maxsize = size
        self.data = [0] * size
        self.length = 0
    def __init__(self, other=None, size=100):
        if other is None:
            self.maxsize = size
            self.data = [0] * size
            self.length = 0
        else:
            self.maxsize = other.maxsize
            self.length = other.length
            self.data = other.data.copy()
    def insertX(self, i, x):
        if i < 0 or i > self.length or self.length >= self.maxsize:
            return
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
if __name__ == "__main__":
    arr1 = Array()
    index = 0
    inputs = list(map(float, input().split()))
    for num in inputs:
        if num == 0:
            break
        arr1.insertX(index, num)
        index += 1
    arr1.displayArray()
    arr2 = Array(arr1)
    arr2.displayArray()
    
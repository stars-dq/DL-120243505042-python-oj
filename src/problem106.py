MaxSize = 100
class Array:
    def __init__(self):
        self.data = [0] * MaxSize
        self.length = 0

    def getLength(self):
        return self.length

    def insertX(self, i, x):
        if i < 0 or i > self.length or self.length >= MaxSize:
            return
        for j in range(self.length, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.length += 1
    def displayArray(self):
        for i in range(self.length):
            num = self.data[i]
            if num.is_integer():
                num = int(num)
            print(num, end=" " if i < self.length - 1 else "\n")
if __name__ == "__main__":
    arr = Array()
    index = 0
    inputs = input().split()
    for num_str in inputs:
        num = float(num_str)
        if num == 0:
            break
        arr.insertX(index, num)
        index += 1
    print(f"Length:{arr.getLength()}")
    print("Elements:", end="")
    arr.displayArray()
    
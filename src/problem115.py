class CString:
    def __init__(self, s=""):
        self.str = s

    def displayString(self):
        print(self.str)

    def mystrlen(self):
        return len(self.str)

    def copy_self(self):
        return CString(self.str)


if __name__ == "__main__":
    input_str = input()
    S1 = CString(input_str)
    S1.displayString()
    print(S1.mystrlen())

    S2 = S1.copy_self()
    S2.displayString()
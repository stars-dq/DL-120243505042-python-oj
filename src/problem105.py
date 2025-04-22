class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def displayComplex(self):
        real_part = self.real if self.real % 1 != 0 else int(self.real)
        imag_part = self.imag if self.imag % 1 != 0 else int(self.imag)
        if self.imag == 0:
            print(real_part)
        elif self.real == 0:
            if imag_part == 1:
                print('i')
            elif imag_part == -1:
                print('-i')
            else:
                print(f'{imag_part}i')
        else:
            if self.imag > 0:
                if imag_part == 1:
                    print(f'{real_part}+i')
                else:
                    print(f'{real_part}+{imag_part}i')
            else:
                if imag_part == -1:
                    print(f'{real_part}-i')
                else:
                    print(f'{real_part}{imag_part}i')


if __name__ == "__main__":
    r1, i1 = map(float, input().split())
    c1 = Complex(r1, i1)
    c1.displayComplex()
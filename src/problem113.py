class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.image = i

    def displayCom(self):
        real_part = round(self.real, 1)
        imag_part = round(self.image, 1)

        if real_part.is_integer():
            real_part = int(real_part)
        if imag_part.is_integer():
            imag_part = int(imag_part)

        if imag_part == 0:
            print(real_part)
        elif imag_part > 0:
            if real_part == 0:
                print(f"{imag_part}i")
            else:
                print(f"{real_part}+{imag_part}i")
        else:
            if real_part == 0:
                print(f"{imag_part}i")
            else:
                print(f"{real_part}{imag_part}i")

    def comAdd(self, c):
        return Complex(self.real + c.real, self.image + c.image)


def comAdd1(c1, c2):
    return Complex(c1.real + c2.real, c1.image + c2.image)


def comAdd2(c1, c2):
    return Complex(c1.real + c2.real, c1.image + c2.image)


if __name__ == "__main__":
    r1, i1,r2,i2 = map(float, input().split())

    c1 = Complex(r1, i1)
    c2 = Complex(r2, i2)
    c3 = Complex()

    c1.displayCom()
    c2.displayCom()
    c3 = c1.comAdd(c2)
    c3.displayCom()

    c3 = comAdd1(c1, c2)
    c3.displayCom()

    c3 = comAdd2(c1, c2)
    c3.displayCom()
    
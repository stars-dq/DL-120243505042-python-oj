class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    def setCom(self, r, i):
        self.real = r
        self.imag = i
    def displayCom(self):
        real_display = int(self.real) if self.real.is_integer() else self.real
        imag_display = int(self.imag) if self.imag.is_integer() else self.imag
        print(f"Complex({real_display},{imag_display})")
if __name__ == "__main__":
    r1, i1 ,r2,i2= map(float, input().split())
    c1 = Complex(r1, i1)
    c2 = Complex()
    c1.displayCom()
    c2.displayCom()
    c2.setCom(r2, i2)
    c2.displayCom()
    
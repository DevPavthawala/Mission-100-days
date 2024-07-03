class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.img = imaginary

    def showNumber(self):
        print(self.real,"i + ",self.img,"j" )

    def __add__(self, num2):  # __add__ -----> dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self, num2):  # __add__ -----> dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)


s1 = Complex(1,5)
s1.showNumber()

s2 = Complex(4,8)
s2.showNumber()

s3 = s1 + s2
s3.showNumber()

s4 = s1 - s2
s4.showNumber()

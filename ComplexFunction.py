import math

class ComplexFunction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def re(self):
        return (self.x*self.x)-(self.y*self.y)

    def im(self):
        return 2*self.x*self.y

    
def ComplexNumber(re, im):
    re = float(re)
    im = float(im)
    if re == 0 and im >=0:
        print('Liczba zespolona : %si' %(im))
    elif re == 0 and im < 0:
        print('Liczba zespolona : %si' %(im))
    elif re > 0 and im < 0:
        print('Liczba zespolona : %s%si' %(re, im))
    elif re < 0 and im < 0:
        print('Liczba zespolona : %s%si' %(re, im))
    else:
        print('Liczba zespolona : %s+%s i' %(re, im))


def Modulus(re, im):
    re = float(re)
    im = float(im)
    return math.sqrt((re*re) + (im*im))

def Argument(re, im):
    re = float(re)
    im = float(im)
    if re > 0:
        return math.atan(im/re)
    elif re < 0 and im >= 0:
        return math.atan(im/re) + math.pi
    elif re < 0 and im < 0:
        return math.atan(im/re) - math.pi
    elif re == 0 and im > 0:
        return math.pi/2
    elif re == 0 and im < 0:
        print('-%s'  %(math.pi/2))
    else:
        print('Independent')             

def main():
    xx=float(input('Podaj x : '))
    x=xx
    yy=float(input('Podaj y : '))
    y=yy
    print('')
    a = ComplexFunction(x, y)
    print('Realis : %s' %(a.re()))
    print('Imaginaris : %s' %(a.im()))                   
    ComplexNumber(a.re(), a.im())
    print('Modulus : %s' %(Modulus(a.re(), a.im())))
    print('Argument : %s' %(Argument(a.re(), a.im())))                     
if __name__ == "__main__":
    main()

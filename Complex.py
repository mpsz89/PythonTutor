import math

def ComplexNumber(re, im):
    re = float(re)
    im = float(im)
    if re == 0 and im >=0:
        print('%s i' %(im))
    elif re == 0 and im < 0:
        print('%s i' %(im))
    elif re > 0 and im < 0:
        print('%s %s i' %(im))
    elif re < 0 and im < 0:
        print('%s %s i' %(im))
    else:
        print('%s + %s i' %(re, im))


def modulus(re, im):
    re = float(re)
    im = float(im)
    return math.sqrt((re*re) + (im*im))

def argument(re, im):
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

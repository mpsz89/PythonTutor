import math

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def poi(k, l):
    k=int(k)
    l=float(l)
    e=float(2.719)
    for i in range(0,k):
        if l > 0:
            return (pow(l, k) * pow(e, (-1 * l))) / fact(k)
        elif l == 0:
            return 0
        else:
            print('Wrong real number !')

def mean(l):
    return math.floor(l)

def median(l):
    return math.floor(l + (1/3) - (0.02/l))

def skewness(l):
    return math.pow(l, (-0.5))

def kurtosis(l):
    return math.pow(l, (-1))

print("ROZKŁAD POISSONA")
print('')
kk=int(input('Ile wystąpień zdarzeń : '))
k=kk
lamb=float(input('Podaj lambdę : '))
l=lamb
print('')
print('Funkcja Rozkładu Prawdopodobieństwa : %s' %(round(poi(k,l), 4)))
print('Moda : %s' %(mean(l)))
print('Mediana : %s' %(median(l)))
print('Współczynnik skośności : %s' %(round(skewness(l), 4)))
print('Wariancja : %s' %(l))
print('Kurtoza : %s' %(round(kurtosis(l), 4)))

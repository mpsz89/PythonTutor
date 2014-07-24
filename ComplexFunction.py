#Michał Piotr Szmigiel
#24 lipca 2014
#Python 3.3.0
#Funkcja zespolona w Pythonie

import math                                             #importowanie pakietu math

class ComplexFunction(object):                          #Tworzenie klasy pythona funkcji zespolonej.
    def __init__(self, x, y):                           #Tworzenie w tej klasie instancji ze zmiennymi x i y.
        self.x = x                                      #Inicjuje zmienne x.
        self.y = y                                      #Inicjuje zmienne y.

    def re(self):                                       #Tworzenie funkcji realisa.
        return (self.x*self.x)-(self.y*self.y)          #Zwraca wynik x^2 - y^2.

    def im(self):                                       #Tworzenie funkcji imaginarisa.
        return 2*self.x*self.y                          #Zwraca wynik 2*x*y.

    
def ComplexNumber(re, im):                              #Tworzenie funkcji imaginarisa.
    re = float(re)                                      #Zmienne realis i imaginaris są równe typom float 
    im = float(im)                                      #czyli typom rzeczywistym.
    if re == 0 and im >=0:                              #Jeżeli realis jest równy 0 i imaginaris większy lub
        print('Liczba zespolona : %si' %(im))           #równy 0 to przepisuje wynik wartości urojonej.
    elif re == 0 and im < 0:                            #W innym przypadku jeżeli realis jest równy 0 i imaginaris 
        print('Liczba zespolona : %si' %(im))           #mniejszy od 0 to przepisuje wynik wartości urojonej.         
    elif re > 0 and im < 0:                             #W innym przypadku jeżeli realis jest wiekszy od 0 i imaginaris
        print('Liczba zespolona : %s%si' %(re, im))     #mniejszy od 0 to przepisuje wynik re-im*i.
    elif re < 0 and im < 0:                             #W innym przypadku jeżeli realis jest mniejszy od 0 i imaginaris
        print('Liczba zespolona : %s%si' %(re, im))     #mniejszy od 0 to przepisuje wynik -re-im*i.
    else:
        print('Liczba zespolona : %s+%s i' %(re, im))   #W ostatnim przypadku zwraca wartość re+im*i


def Modulus(re, im):                                    #Tworzenie funkcji modułu zespolonego.
    re = float(re)                                      #Zmienne realis i imaginaris są równe typom float.
    im = float(im)
    return math.sqrt((re*re) + (im*im))                 #Zwraca wynik znany ze stwierdzenia Pitagorasa sqrt(re^2 + im^2).

def Argument(re, im):                                   #Tworzenie funkcji argumentu.
    re = float(re)                                      #Zmienne realis i imaginaris są równe typom float.
    im = float(im)
    if re > 0:                                          #Jeżeli realis > 0 to zwraca wynik arctan(re/im).                                
        return math.atan(im/re)
    elif re < 0 and im >= 0:                            #W innym przypadku jeżeli realis < 0 i imaginaris >= 0 to zwraca wynik arctan(re/im) + pi.
        return math.atan(im/re) + math.pi
    elif re < 0 and im < 0:                             #W innym przypadku jeżeli realis < 0 i imaginaris < 0 to zwraca wynik arctan(re/im) - pi.
        return math.atan(im/re) - math.pi
    elif re == 0 and im > 0:                            #W innym przypadku jeżeli realis = 0 i imaginaris > 0 to zwraca wynik pi/2.
        return math.pi/2
    elif re == 0 and im < 0:                            #W innym przypadku jeżeli realis = 0 i imaginaris < 0 to zwraca wynik -pi/2.
        print('-%s'  %(math.pi/2))
    else:                                               #W ostatnim przypadku wartość jest niezdefiniowana.
        print('Independent')             

def main():                                             #Tworzenie głównego programu.
    xx=float(input('Podaj x : '))                       #Zmienne xx jest równy typom float z podawaniem wartości wyjściowej x.
    x=xx                                                #zmienne x = xx.
    yy=float(input('Podaj y : '))                       #Zmienne yy jest równy typom float z podawaniem wartości wyjściowej y.
    y=yy                                                #zmienne y = yy.
    print('')
    a = ComplexFunction(x, y)                           #Tworzenie obiektu z klasy funkcji zespolonej.
    print('Realis : %s' %(a.re()))                      #Przepisanie wartości wejściowej realisa.
    print('Imaginaris : %s' %(a.im()))                  #Przepisanie wartości wejściowej imaginarisa.                
    ComplexNumber(a.re(), a.im())                       #Przepisanie wartości wejściowej liczby zespolonej.
    print('Modulus : %s' %(Modulus(a.re(), a.im())))    #Przepisanie wartości wejściowej modułu.
    print('Argument : %s' %(Argument(a.re(), a.im())))  #Przepisanie wartości wejściowej argumentu.                 
if __name__ == "__main__":                              #Sprawdzenie jeżeli moduł __name__ równy modułu "__main__" to zwróci funkcję main().
    main()

#Michał Piotr Szmigiel
#15 marca 2014
#Python 3.3.0
#Podsilnia w Pythonie

def fact(n):                                    #Tworzenie funkcji silnii
    if n == 0:                                  #Jeżeli n = 0 zwraca wynik 1
        return 1
    else:                                       #W innym przypadku zwraca wynik n * fact(n-1)
        return n * fact(n-1)

def subfact_rec(n):                             #Tworzenie funkcji podsilnii w wersji rekurencyjnej
    if n == 0:                                  #Jeżeli n = 0 zwraca wynik 1
        return 1
    else:
        return n * fact(n-1) + pow((-1), n)     #W innym przypadku zwraca wynik n * fact(n-1) - 1^n

def subfact(n):                                 #Tworzenie funkcji podsilnii w prostej wersji
    e=2.719                                     #Zmienne e jest potraktowane jako logarytm naturalny równy 2.719
    return round(fact(n) / e)                   #Zwraca wynik zaokrąglenia do liczy calkowitej ilorazu silnii i e
                                                

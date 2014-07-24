#Michał Piotr Szmigiel
#28 lutego 2014
#Python 3.3.0
#Stała Erdos/Borwein w Pythonie

def ErdosBorwein(i):                    #Tworzenie funkcji stałej Erdos/Borwein
    e = 0                               #Zmienne e zaczyna się od równego 0
    for n in range(1, i):               #W petli for dla zmiennej n = 1 do zmiennej i
        e += 1 / (pow(2, n) - 1)        #Sumowanie e = e + 1/(2^n - 1)
    return e                            #Zwraca wynik e

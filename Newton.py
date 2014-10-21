#Michał Piotr Szmigiel
#21 październik 2014
#Python 3.3.0
#Dwumian Newtona w Pythonie

#Tworzenie funkcji silni
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

#Tworzenie funkcji dwumianu Newtona  
def newton(n, k):
    n=float(n)
    k=float(k)
    if n > k:
        return fact(n) / (fact(n - k) * fact(k))
    elif n == k:
        print('Nieskończoność')
    else:
        print('Błędne twierdzenie obliczeniowe')

#Tworzenie programu głównego
def main():
    nn=float(input('Podaj n : '))
    n=nn
    kk=float(input('Podaj k : '))
    k=kk
    print(newton(n, k))
if __name__ == "__main__":                              
    main()

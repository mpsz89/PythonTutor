#Michał Piotr Szmigiel
#9 sierpnia 2014
#Python 3.3.0
#Funkcja boolowska w Pythonie

#Tworzenie funkcji boolowskej, opartej na tablicy prawdy
def BoolFun(x, y, z):
    log = '10-'
    a, b, c = log
    if x == 0 and y == 0 and z == 0:
        print(a)
    elif x == 0 and y == 0 and z ==1:
        print(a)    
    elif x == 0 and y == 1 and z ==0:
        print(a)
    elif x == 0 and y == 1 and z ==1:
        print(c)
    elif x == 1 and y == 0 and z ==0:
        print(a)
    elif x == 1 and y == 0 and z ==1:
        print(b)
    elif x == 1 and y == 1 and z ==0:
        print(a)
    elif x == 1 and y == 1 and z ==1:
        print(b)
    else:
        print('logical value error')

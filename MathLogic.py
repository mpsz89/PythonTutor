#Michał Piotr Szmigiel
#10 kwietnia 2013
#Python 3.3.0
#Logika matematyczna w Pythonie

#Tworzenie funkcji alternatywy, czyli na zasadzie p lub q
def alt(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return True
    elif p==1 and q==0:
        return True
    elif p==0 and q==1:
        return True
    elif p==0 and q==0:
        return False
    else:
        print('logical value error !!!')

#Tworzenie funkcji koniunkcji, czyli na zasadzie p i q
def con(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return True
    elif p==1 and q==0:
        return False
    elif p==0 and q==1:
        return False
    elif p==0 and q==0:
        return False
    else:
        print('logical value error !!!')

#Tworzenie funkcji implikacji, czyli na zasadzie p wynika z q
def imp(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return True
    elif p==1 and q==0:
        return False
    elif p==0 and q==1:
        return True
    elif p==0 and q==0:
        return True
    else:
        print('logical value error !!!')

#Tworzenie funkcji równoważności, czyli na zasadzie p wtedy i tylko wtedy, gdy q
def iff(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return True
    elif p==1 and q==0:
        return False
    elif p==0 and q==1:
        return False
    elif p==0 and q==0:
        return True
    else:
        print('logical value error !!!')

#Tworzenie funkcji dysjunkcji, czyli zaprzeczania koniunkcji
def nand(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return False
    elif p==1 and q==0:
        return True
    elif p==0 and q==1:
        return True
    elif p==0 and q==0:
        return True
    else:
        print('logical value error !!!')

#Tworzenie funkcji alternatywy wykluczającej, czyli na zasadzie p albo q
def xor(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return False
    elif p==1 and q==0:
        return True
    elif p==0 and q==1:
        return True
    elif p==0 and q==0:
        return False
    else:
        print('logical value error !!!')

#Tworzenie funkcji binegacji, czyli zaprzeczania alternatywy
def nor(p,q):
    p=int(p)
    q=int(q)
    if p==1 and q==1:
        return False
    elif p==1 and q==0:
        return False
    elif p==0 and q==1:
        return False
    elif p==0 and q==0:
        return True
    else:
        print('logical value error !!!')

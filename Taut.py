#Michał Piotr Szmigiel
#10 sierpnia 2014
#Python 3.3.0
#Tautologia rachunku zdań w Pythonie

#Tworzenie funkcji negującej, czyli na zasadzie "nie prawda, że..."
def neg(a):
    if a==1:
        return 0
    else:
        return 1
       
#Tworzenie funkcji alternatywy, czyli na zasadzie p lub q
def alt(p,q):
    if p==1 and q==1:
        return 1
    elif p==1 and q==0:
        return 1
    elif p==0 and q==1:
        return 1
    elif p==0 and q==0:
        return 0
    else:
        print('logical value error !!!')

#Tworzenie funkcji koniunkcji, czyli na zasadzie p i q
def con(p,q):
    if p==1 and q==1:
        return 1
    elif p==1 and q==0:
        return 0
    elif p==0 and q==1:
        return 0
    elif p==0 and q==0:
        return 0
    else:
        print('logical value error !!!')

#Tworzenie funkcji implikacji, czyli na zasadzie p wynika z q
def imp(p,q):
    if p==1 and q==1:
        return 1
    elif p==1 and q==0:
        return 0
    elif p==0 and q==1:
        return 1
    elif p==0 and q==0:
        return 1
    else:
        print('logical value error !!!')

#Tworzenie funkcji dysjunkcji, czyli zaprzeczanie koniunkcji
def nand(p,q):
    if p==1 and q==1:
        return 0
    elif p==1 and q==0:
        return 1
    elif p==0 and q==1:
        return 1
    elif p==0 and q==0:
        return 1
    else:
        print('logical value error !!!')

#Modus tollendo ponens (łac. sposób potwierdzający przez zaprzeczenie)
def MTP(p,q):
    return imp(con(alt(p,q), neg(p)), q)

#Modus ponendo ponens (łac. sposób potwierdzający przez potwierdzenie)
def MPP(p,q):
    return imp(con(imp(p,q), p), q)

#Modus ponendo tollens (łac. sposób zaprzeczający przez potwierdzenie)
def MPT(p,q):
    return imp(con(nand(p,q), p), neg(q))

#Modus tollens (modus tollendo tollens, łac. sposób zaprzeczający przy pomocy zaprzeczenia)
def MT(p,q):
    return imp(con(imp(p,q), neg(q)), neg(p))


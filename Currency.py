#Michał Piotr Szmigiel
#20 sierpnia 2014
#Python 3.3.0
#Kurs walut w Pythonie

#Tworzenie klasy, której przelicza ze złotych na euro
class PLNtoEURO(object):
    def __init__(self, pln):
        self.pln = pln
        

    def PLtoEU(self):
        if self.pln >= 0:
            return round(self.pln * 0.238329742, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z eura na złote
class EUROtoPLN(object):
    def __init__(self, euro):
        self.euro = euro
        

    def EUtoPL(self):
        if self.euro >= 0:
            return round(self.euro * 4.19586742, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza ze złotych na funty
class PLNtoGBP(object):
    def __init__(self, pln):
        self.pln = pln
        

    def PLtoGB(self):
        if self.pln >= 0:
            return round(self.pln * 0.702264899, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza ze funta na złote
class GBPtoPLN(object):
    def __init__(self, gbp):
        self.gbp = gbp
        

    def GBtoPL(self):
        if self.gbp >= 0:
            return round(self.gbp * 5.28143855, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z eura na funty
class EUROtoGBP(object):
    def __init__(self, euro):
        self.euro = euro
        

    def EUtoGB(self):
        if self.euro >= 0:
            return round(self.euro * 2.94661041, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza ze funta na euro
class GBPtoEURO(object):
    def __init__(self, gbp):
        self.gbp = gbp
        

    def GBtoEU(self):
        if self.gbp >= 0:
            return round(self.gbp * 1.25872389, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza ze złotych na franki szwajcarskie
class PLNtoCHF(object):
    def __init__(self, pln):
        self.pln = pln
        

    def PLtoCH(self):
        if self.pln >= 0:
            return round(self.pln * 0.289405097, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z franka szwajcarskiego na złote
class CHFtoPLN(object):
    def __init__(self, chf):
        self.chf = chf
        

    def CHtoPL(self):
        if self.chf >= 0:
            return round(self.chf * 3.45536417, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z eura na franki szwajcarskie
class EUROtoCHF(object):
    def __init__(self, euro):
        self.euro = euro
        

    def EUtoCH(self):
        if self.euro >= 0:
            return round(self.euro * 1.21137209, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z franka szwajcarskiego na euro
class CHFtoEURO(object):
    def __init__(self, chf):
        self.chf = chf
        

    def CHtoEU(self):
        if self.chf >= 0:
            return round(self.chf * 0.825510189, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z funta na franki szwajcarskie
class GBPtoCHF(object):
    def __init__(self, gbp):
        self.gbp = gbp
        

    def GBtoCH(self):
        if self.gbp >= 0:
            return round(self.gbp * 1.51642786, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie klasy, której przelicza z franka szwajcarskiego na funty
class CHFtoGBP(object):
    def __init__(self, chf):
        self.chf = chf
        

    def CHtoGB(self):
        if self.chf >= 0:
            return round(self.chf * 0.665383069, 2)
        else:
            print('Value of currency error !!!')

#Tworzenie funkcji, ktorej ma wybrać walute do przeliczenia
def currency(z, na):
    if z == 1 and na == 2:
        print('Ze złotych na euro')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        a = PLNtoEURO(val)
        print('%s PLN = %s EURO' %(val, a.PLtoEU()))
    elif z == 2 and na == 1:
        print('Z euro na złote')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        b = EUROtoPLN(val)
        print('%s EURO = %s PLN' %(val, b.EUtoPL()))
    elif z == 1 and na == 3:
        print('Ze złotych na funty')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        c = PLNtoGBP(val)
        print('%s PLN = %s GBP' %(val, c.PLtoGB()))
    elif z == 3 and na == 1:
        print('Z funta na złote')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        d = GBPtoPLN(val)
        print('%s GBP = %s PLN' %(val, d.GBtoPL()))
    elif z == 1 and na == 4:
        print('Ze złotych na frank szwajczarski')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        e = PLNtoCHF(val)
        print('%s PLN = %s CHF' %(val, e.PLtoCH()))
    elif z == 4 and na == 1:
        print('Z franka szwajcarskiego na złote')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        f = CHFtoPLN(val)
        print('%s CHF = %s PLN' %(val, f.CHtoPL()))
    elif z == 2 and na == 3:
        print('Z euro na funty')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        g = EUROtoGBP(val)
        print('%s EURO = %s GBP' %(val, g.EUtoGB()))
    elif z == 3 and na == 2:
        print('Z funta na euro')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        h = GBPtoEURO(val)
        print('%s GBP = %s EURO' %(val, h.GBtoEU()))
    elif z == 2 and na == 4:
        print('Z euro na frank szwajcarski')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        i = EUROtoCHF(val)
        print('%s EURO = %s CHF' %(val, i.EUtoCH()))
    elif z == 4 and na == 2:
        print('Z franka szwajcarskiego na euro')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        j = CHFtoEURO(val)
        print('%s CHF = %s EURO' %(val, j.CHtoEU()))
    elif z == 3 and na == 4:
        print('Z funta na frank szwajcarski')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        k = GBPtoCHF(val)
        print('%s GBP = %s CHF' %(val, k.GBtoCH()))
    elif z == 4 and na == 3:
        print('Z franka szwajcarskiego na funt')
        v=(int(input('Podaj wartość pieniężna : ')))
        val=v
        l = CHFtoEURO(val)
        print('%s CHF = %s GBP' %(val, l.CHtoGB()))
    elif ( z == 1 and na == 1 ) or ( z == 2 and na == 2 ) or ( z == 3 and na == 3 ) or ( z == 3 and na == 3 ):
        print('Entering currency error !!!')
    else:
        print('Choosing of currency error !!!')

#Tworzenie funkcji programu głównego, wraz z funkcją walutową
def main():
    print('1 - PLN')
    print('2 - EURO')
    print('3 - GBP')
    print('4 - CHF')
    od=(int(input('Podaj walutę : ')))
    z=od
    do=(int(input('Na jaka walutę chcesz obliczyć : ')))
    na=do
    currency(z, na)

if __name__ == '__main__':
    main() 
    

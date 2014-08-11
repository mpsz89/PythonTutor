#Michał Piotr Szmigiel
#28 lutego 2014
#Python 3.3.0
#Liczba zespolona w Pythonie

#importowanie modułu math
import math                                             

#Tworzenie funkcji liczby zespolonej
def ComplexNumber(re, im):                              
    re = float(re)                                       
    im = float(im)                                      
    if re == 0 and im >=0:                              
        print('Liczba zespolona : %si' %(im))           
    elif re == 0 and im < 0:                             
        print('Liczba zespolona : %si' %(im))                  
    elif re > 0 and im < 0:                             
        print('Liczba zespolona : %s%si' %(re, im))     
    elif re < 0 and im < 0:                             
        print('Liczba zespolona : %s%si' %(re, im))     
    else:
        print('Liczba zespolona : %s+%s i' %(re, im))   


#Tworzenie funkcji modułu zespolonego.
def Modulus(re, im):                                    
    re = float(re)                                      
    im = float(im)
    return math.sqrt((re*re) + (im*im))                 

#Tworzenie funkcji argumentu.
def Argument(re, im):                                   
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

def Literal(x):
    if x == 'x':
        return 1
    elif x == '|x':
        return 0
    elif x == '1':
        return '-'
    else:
        ('Wrong literal')

def var3(a,b,c):
    a=str(a)
    b=str(b)
    c=str(c)
    print('%s %s %s' %(Literal(a), Literal(b), Literal(c)))
          
def var4(a,b,c,d):
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    print('%s %s %s %s' %(Literal(a), Literal(b), Literal(c), Literal(d)))        

def var5(a,b,c,d,e):
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    e=str(e)
    print('%s %s %s %s %s' %(Literal(a), Literal(b), Literal(c), Literal(d), Literal(e)))
              
def var6(a,b,c,d,e,f):
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    e=str(e)
    f=str(f)
    print('%s %s %s %s %s %s' %(Literal(a), Literal(b), Literal(c), Literal(d), Literal(e), Litera(f)))

def var7(a,b,c,d,e,f,g):
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    e=str(e)
    f=str(f)
    g=str(g)
    print('%s %s %s %s %s %s' %(Literal(a), Literal(b), Literal(c), Literal(d), Literal(e), Literal(f), Literal(g)))

def var8(a,b,c,d,e,f,g,h):
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    e=str(e)
    f=str(f)
    g=str(g)
    h=str(h)
    print('%s %s %s %s %s %s' %(Literal(a), Literal(b), Literal(c), Literal(d), Literal(e), Literal(f), Literal(g), Literal(h)))

def BooleanFunction(n):
          if n == 3:
              aa = str(input('Enter the first literal : '))
              a=aa
              bb = str(input('Enter the second literal : '))
              b=bb
              cc = str(input('Enter the last literal : '))
              c=cc
              var3(a,b,c)            
          elif n == 4:
              aa = str(input('Enter the first literal : '))
              a=aa
              bb = str(input('Enter the second literal : '))
              b=bb
              cc = str(input('Enter the third literal : '))
              c=cc
              dd = str(input('Enter the last literal : '))
              d=dd
              var4(a,b,c,d)
          elif n == 5:
              aa = str(input('Enter the first literal : '))
              a=aa
              bb = str(input('Enter the second literal : '))
              b=bb
              cc = str(input('Enter the third literal : '))
              c=cc
              dd = str(input('Enter the fourth literal : '))
              d=dd
              ee = str(input('Enter the last literal : '))
              e=ee
              var5(a,b,c,d,e)
          elif n == 6:
              aa = str(input('Enter the first literal : '))
              a=aa
              bb = str(input('Enter the second literal : '))
              b=bb
              cc = str(input('Enter the third literal : '))
              c=cc
              dd = str(input('Enter the fourth literal : '))
              d=dd
              ee = str(input('Enter the fifth literal : '))
              e=ee
              ff = str(input('Enter the last literal : '))
              f=ff
              var6(a,b,c,d,e,f)
          elif n == 7:
              aa = str(input('Enter the first literal : '))
              a=aa
              bb = str(input('Enter the second literal : '))
              b=bb
              cc = str(input('Enter the third literal : '))
              c=cc
              dd = str(input('Enter the fourth literal : '))
              d=dd
              ee = str(input('Enter the fifth literal : '))
              e=ee
              ff = str(input('Enter the sixth literal : '))
              f=ff
              gg = str(input('Enter the last literal : '))
              g=gg
              var7(a,b,c,d,e,f,g)
          elif n == 8:
              aa = str(input('Enter the first literal : '))
              a=aa
              bb = str(input('Enter the second literal : '))
              b=bb
              cc = str(input('Enter the third literal : '))
              c=cc
              dd = str(input('Enter the fourth literal : '))
              d=dd
              ee = str(input('Enter the fifth literal : '))
              e=ee
              ff = str(input('Enter the sixth literal : '))
              f=ff
              gg = str(input('Enter the seventh literal : '))
              g=gg
              hh = str(input('Enter the last literal : '))
              h=hh
              var8(a,b,c,d,e,f,g,h)
          else:
              print('Wrong number of variables')
          
          

def BooleanSum(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 1
    elif a == 0 and b == 0 and c == 1:
        return 1
    elif a == 0 and b == 1 and c == 0:
        return 1
    elif a == 0 and b == 1 and c == 1:
        print('-')
    elif a == 1 and b == 0 and c == 0:
        return 1
    elif a == 1 and b == 0 and c == 1:
        return 0
    elif a == 1 and b == 1 and c == 0:
        return 1
    elif a == 1 and b == 1 and c == 1:
        return 0
    else:
        print('Wrong logical value')


    
        

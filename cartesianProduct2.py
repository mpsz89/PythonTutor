def kartez2(a,b,c,d):    
    print("A x B = { ")
    for i in range(a, b+1):
        for j in range(c, d+1):
            print("( %s, %s )" %(i, j))
            if i<b or j<d:
                print(", ")
    print(" }")

def kartez3(a,b,c,d,e,f):   
    print("A x B x C = { ")
    for i in range(a, b+1):
        for j in range(c, d+1):
            for k in range(e, f+1):
                print("( %s, %s, %s )" %(i, j, k))
                if i<b or j<d or k<f:
                    print(", ")
    print(" }")

def kartez4(a,b,c,d,e,f,g,h):   
    print("A x B x C x D = { ")
    for i in range(a, b+1):
        for j in range(c, d+1):
            for k in range(e, f+1):
                for l in range(g, h+1):
                    print("( %s, %s, %s, %s )" %(i, j, k, l))
                    if i<b or j<d or k<f or l<h:
                        print(", ")
    print(" }")

def set2():
    print("Dla zbioru A")
    p=int(input("Podaj wartość początkowa : "))
    a=p
    k=int(input("Podaj wartość końcowa : "))
    b=k
    print(" ")
    print("Dla zbioru B")
    p1=int(input("Podaj wartość początkowa : "))
    c=p1
    k1=int(input("Podaj wartość końcowa : "))
    d=k1
    print(" ")
    kartez2(a,b,c,d)

    
def set3():
    print("Dla zbioru A")
    p=int(input("Podaj wartość początkowa : "))
    a=p
    k=int(input("Podaj wartość końcowa : "))
    b=k
    print(" ")
    print("Dla zbioru B")
    p1=int(input("Podaj wartość początkowa : "))
    c=p1
    k1=int(input("Podaj wartość końcowa : "))
    d=k1
    print(" ")
    print("Dla zbioru C")
    p2=int(input("Podaj wartość początkowa : "))
    e=p2
    k2=int(input("Podaj wartość końcowa : "))
    f=k2
    print(" ")
    kartez3(a,b,c,d,e,f)

def set4():
    print("Dla zbioru A")
    p=int(input("Podaj wartość początkowa : "))
    a=p
    k=int(input("Podaj wartość końcowa : "))
    b=k
    print(" ")
    print("Dla zbioru B")
    p1=int(input("Podaj wartość początkowa : "))
    c=p1
    k1=int(input("Podaj wartość końcowa : "))
    d=k1
    print(" ")
    print("Dla zbioru C")
    p2=int(input("Podaj wartość początkowa : "))
    e=p2
    k2=int(input("Podaj wartość końcowa : "))
    f=k2
    print(" ")
    print("Dla zbioru D")
    p3=int(input("Podaj wartość początkowa : "))
    g=p3
    k3=int(input("Podaj wartość końcowa : "))
    h=k3
    print(" ")
    kartez4(a,b,c,d,e,f,g,h)

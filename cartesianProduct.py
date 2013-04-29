def kartez(a,b,c,d):
    print("A x B = { ")
    for i in range(a, b+1):
        for j in range(c, d+1):
            print("( %s, %s )" %(i, j))
            if i<b or j<d:
                print(", ")
    print(" }")

print("Dla zbioru A")
p=int(input("Podaj wartość początkowa : "))
a=p
k=int(input("Podaj wartość końcowa : "))
b=k
print(" ")
print("Dla zbioru B")
pp=int(input("Podaj wartość początkowa : "))
c=pp
kk=int(input("Podaj wartość końcowa : "))
d=kk
print(" ")
kartez(a,b,c,d)

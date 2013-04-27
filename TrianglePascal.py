def nCr(n,k):
        n=int(n)
        k=int(k)
        if n==k:
                return 1
        else:
                return fact(n) / (fact(n-k) * fact(k))

def fact(i):
        i=int(i)
        val = 1
        if i!=0:
                for j in range(2,i+1):
                        val = val * j
        return val
         

def pascal(n):
        n=int(n)
        print(' ')
        for i in range(0,n):
                print(' ')
                for j in range(0,i+1):
                        print(nCr(i,j))
        print(' ')


l=int(input("Enter the natural number : "))
m=l
print(pascal(m))

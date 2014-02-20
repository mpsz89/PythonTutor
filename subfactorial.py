def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def subfact_rec(n):
    #rekurencyjna definicja podsilni
    if n == 0:
        return 1
    else:
        return n * fact(n-1) + pow((-1), n) 

def subfact(n):
    e=2.719
    return round(fact(n) / e)

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

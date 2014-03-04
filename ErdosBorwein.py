def ErdosBorwein(i):
    e = 0
    for n in range(1, i):
        e += 1 / (pow(2, n) - 1)
    return e

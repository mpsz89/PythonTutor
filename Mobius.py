def mobius(n):
    result, i = 1, 2
    while n >= i:
        if n % i == 0:
            n = n / i
            if n % i == 0:
                return 0
            result = -result
        i = i + 1
    return result

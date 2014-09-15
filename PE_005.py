def PE_005():
    factors = []    # contains all prime factors
    max = 20

    for i in range (1, max):
        # gets list of prime factors
        newFactors = getPrimes(i + 1)

        tmp = factors[:]
        # adds prime factors to factors if not already there
        for num in newFactors:
            if num in tmp:
                tmp.remove(num)
            else:
                factors.append(num)

    product = 1
    for f in factors:
        product *= f
    return product

def getPrimes(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n /= d
        d += 1
    if n > 1:
       factors.append(n)
    return factors

print (PE_005())
def PE_012():
    maxPrime = 10000
    triNum = 0
    n = 1

    primes = getPrimes(maxPrime)    # get all primes up to 10,000

    while (getFactors(triNum, primes) < 500):
        triNum += n
        n += 1
    return triNum

# sieve of eratosthenes
def getPrimes (max):
    li = [True] * max
    li[0] = False
    li[1] = False

    for i in range (0, int(math.sqrt(max))):
        if li[i] == True:
            factor = i * 2
            while (factor < max):
                li[factor] = False
                factor += i

    primes = []
    for i in range (0, max):
        if li[i] == True:
            primes.append(i)

    return primes

def getFactors(n, primes):
    count = 1
    exp = 1
    remainder = n

    if n == 0 or n == 1:
        return 1

    for i in xrange(0, len(primes)):
        # if remainder
        if primes[i] * primes[i] > n:
            return count * 2

        # count that prime factor
        exp = 1
        while (remainder % primes[i]) == 0:
            exp += 1
            remainder /= primes[i]

        count *= exp

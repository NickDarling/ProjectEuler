def PE_010():
    max = 2000000
    li = [True] * max
    li[0] = False
    li[1] = False

    for i in range (0, int(math.sqrt(max))):
        if li[i] == True:
            factor = i * 2
            while (factor < max):
                li[factor] = False
                factor += i

    sum = 0
    for i in range (0, max):
        if li[i] == True:
            sum += i

    return sum
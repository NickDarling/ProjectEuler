def PE_002():
    term1 = 1
    term2 = 2
    sum = 0

    while (term2 < 4000000):
        if (term2 % 2 == 0):
            sum += term2
        term2 += term1
        term1 = term2 - term1
    return sum

print (PE_002())
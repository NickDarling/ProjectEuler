def PE_003():
    num = 600851475143
    factor = 1

    while (factor < num):
        factor += 2;
        while (num % factor == 0):
            num /= factor

    return factor;

print (PE_003())
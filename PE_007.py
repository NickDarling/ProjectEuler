import math

def PE_007():
    index = 10001
    i = 1
    prime = True

    while (index > 1):
        i += 2
        prime = True

        for num in range (2, int(math.sqrt(i) + 1)):
            if (i % num == 0):
                prime = False
                break
        if (prime):
            index -= 1
    return i

print (PE_007())
def PE_009():
    sum = 1000

    for A in range (1, sum):
        for B in range (A, sum):
            C = sum - A - B
            if (A * A + B * B) == (C * C):
                return A * B * C

print (PE_009())
def PE_004():
    max = 0
    curr = 0

    for num1 in range (100, 1000, 1):
        for num2 in range(100, 1000, 1):
            curr = num1 * num2
            if (str(curr) == str(curr)[::-1] and curr > max):
                max = curr
    return max
    
print (PE_004())
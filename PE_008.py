def PE_008():
    f = open ('PE_008_input.txt', 'r')
    max = -1
    digits = ''

    for line in f:
        digits += line[:-1]

    start = 0
    end = 13

    while (end <= 1000):
        currDigit = digits[start:end]
        if str(0) not in currDigit:
            product = 1
            for i in range(0, len(currDigit)):
                product *= int(currDigit[i])
            if product > max:
                max = product
        start += 1
        end += 1
    return max

print (str(PE_008()))
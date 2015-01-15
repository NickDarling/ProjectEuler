def PE_013():
    f = open ('PE_013_input.txt', 'r')

    length = 50
    curr = length - 1

    result = ""
    numbers = []

    # line[:-1] to get rid of \n
    for line in f:
        numbers.append(line[:-1])

    carry = 0
    for i in xrange(0, length):
        for num in numbers:
            # add one decimal place at at time
            carry += int(num[curr])
        curr -= 1
        result = str(carry)[-1:] + result
        carry /= 10
    result = str(carry) + result

    print len(result)
    return result
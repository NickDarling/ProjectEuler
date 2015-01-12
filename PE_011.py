def PE_011():
    f = open ('PE_011_input.txt', 'r')

    length = 20
    max = 0
    grid = []

    # line[:-1] to get rid of \n
    for line in f:
        grid.append([int(x) for x in (line[:-1].split(" "))])

    for i in xrange(length):
        # horizontal
        row = i
        for index in xrange(length):
            if index < (length - 3):
                product = 1
                for j in xrange(4):
                    product *= grid[row][index + j]
                if product > max:
                    max = product

        # vertical
        col = i
        for index in xrange(length):
            if index < (length - 3):
                product = 1
                for j in xrange(4):
                    product *= grid[index + j][col]
                if product > max:
                    max = product

        # diagonal right
        row = i
        for index in xrange(length):
            if index < (length - 3) and row < (length - 3):
                product = 1
                for j in xrange(4):
                    product *= grid[row + j][index + j]
                if product > max:
                    max = product

        # diagonal left
        row = i
        for index in xrange(length):
            if index > 2 and row < (length - 3):
                product = 1
                for j in xrange(4):
                    product *= grid[row + j][index - j]
                if product > max:
                    max = product

    return max
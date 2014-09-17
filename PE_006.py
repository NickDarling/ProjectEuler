def PE_006():
    sumOfSquares = 0
    squareofSums = 0

    for i in range (1, 101):
        sumOfSquares +=(i * i)

    for i in range (1, 101):
        squareofSums += i

    return (squareofSums * squareofSums - sumOfSquares)

print (PE_006())
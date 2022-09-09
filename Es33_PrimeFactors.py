def factors(value):
    fattori = []
    i = 2
    while i - 1 < value:
        while value % i == 0:
            fattori.append(i)
            value /= i
        i+=1
    return fattori
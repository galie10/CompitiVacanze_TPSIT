def sum_of_multiples(limit, multiples):
    somma = 0
    if 0 in multiples:
        multiples.remove(0)
    for i in range(1,limit):
        for multiplo in multiples:
            if not (i % multiplo):
                somma += i
                break
    
    return somma
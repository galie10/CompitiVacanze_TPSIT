def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    integer = 1
    primi = []
    if primi:
        integer = primi[-1]
    while len(primi) < number:
        integer += 1
        primo_dopo = True
        indice = 0
        while primo_dopo and indice < len(primi):
            if integer % primi[indice] == 0:
                primo_dopo = False
            else:
                indice += 1
        if primo_dopo:
            primi.append(integer)
    return primi[-1]
def is_armstrong_number(number):
    num_cifre = len(str(number))
    totale = 0
    for cifre in str(number):
        totale += (int(cifre) ** num_cifre)
    if totale == number:
        return True
    else: return False
from math import sqrt
def score(x, y):
    distanza = sqrt(x*x + y*y)
    
    if distanza > 10:
        return 0
    elif distanza > 5:
        return 1
    elif distanza > 1:
        return 5
    else: 
        return 10

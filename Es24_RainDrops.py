def convert(number):
    gocce = ""
    if number % 3 == 0:
        gocce += "Pling"
    if number % 5 == 0:
        gocce += "Plang"
    if number % 7 == 0:
        gocce += "Plong"
    return gocce or f"{number}"
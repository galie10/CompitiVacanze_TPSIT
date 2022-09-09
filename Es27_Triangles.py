def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a != 0 or b != 0 or c != 0:
        if a + b >= c:
            if b + c >= a:
                if a + c >= b:
                    if a == b and b == c and c == a:
                        return True
                    else: return False
                else: return False
            else:return False
        else: return False
    else: return False
def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b >= c:
        if b + c >= a:
            if a + c >= b:
                if a == b or b == c or a == c:
                    return True
                else: return False
            else: return False
        else:return False
    else: return False
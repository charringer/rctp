
def lcm(a,b=None):
    """
    least common multiple
    """
    if b == None:
        if len(a) == 0:
            return 0
        elif len(a) == 1:
            return a[0]
        else:
            return lcm(a[0],lcm(a[1:]))
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a*b)//gcd(a,b)

def gcd(a,b=None):
    """
    greatest common divisor
    """
    if b == None:
        if len(a) == 0:
            return 0
        elif len(a) == 1:
            return abs(a[0])
        else:
            return gcd(gcd(a[0],a[1]), gcd(a[2:]))
    if a < 0: a = -a
    if b < 0: b = -b 
    while True:
        if b > a:
            a, b = b, a
        if b == 0:
            return a
        a -= b

# vim:expandtab:softtabstop=4:shiftwidth=4

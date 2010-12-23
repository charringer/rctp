
def lcm(a,b):
    """
    least common multiple
    """
    return a*b/gcd(a,b)

def gcd(a,b):
    """
    greatest common divisor
    """
    if a < 0: a = -a
    if b < 0: b = -b 
    while True:
        if b > a:
            a, b = b, a
        if b == 0:
            return a
        a -= b

# vim:expandtab:softtabstop=4:shiftwidth=4

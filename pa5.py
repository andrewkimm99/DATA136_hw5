import math

def gcd(a, b):
    if b > a:
        temp = b
        b = a
        a = temp
    if b == 0:
        return a
    return gcd(b, a%b)

def remove_pairs(s):
    uturn_l = ['SN', 'NS', 'WE', 'EW']
    if len(s) < 2:
        return s
    if s[:2] in uturn_l:   
        return remove_pairs(s[2:])
    else:
        return s[0] + remove_pairs(s[1:])

def bisection_root(f, x1, x2):
    if abs(f(x1)) <= 0.001:
        return x1
    elif abs(f(x2)) <= 0.001:
        return x2
    midpoint = (x1 + x2) / 2
    if f(midpoint) < 0:
        if f(x2) > 0:
            return bisection_root(f, midpoint, x2)
        elif f(x1) > 0:
            return bisection_root(f, midpoint, x1)
        else:
            raise ValueError("Both x values have same sign")
    elif f(midpoint) > 0:
        if f(x2) < 0:
            return bisection_root(f, midpoint, x2)
        elif f(x1) < 0:
            return bisection_root(f, midpoint, x1)
        else:
            raise ValueError("Both x values have same sign")





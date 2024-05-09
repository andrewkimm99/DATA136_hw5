'''
hw5
'''
import math

def gcd(a, b):
    '''
    do gcd using recursion
    '''
    if b > a:
        temp = b
        b = a
        a = temp
    if b == 0:
        return a
    return gcd(b, a%b)

def remove_pairs(s):
    '''
    remove pairs using recursion
    '''
    uturn_l = ['SN', 'NS', 'WE', 'EW']
    if len(s) < 2:
        return s
    if s[:2] in uturn_l:
        return remove_pairs(s[2:])
    return s[0] + remove_pairs(s[1:])

def bisection_root(f, x_1, x_2):
    '''
    find function root using bisection and recursion
    '''
    if abs(f(x_1)) <= 0.0000001:
        return x_1
    if abs(f(x_2)) <= 0.0000001:
        return x_2
    midpoint = (x_1 + x_2) / 2
    if f(midpoint) < 0:
        if f(x_2) > 0:
            return bisection_root(f, midpoint, x_2)
        elif f(x_1) > 0:
            return bisection_root(f, midpoint, x_1)
        else:
            raise ValueError("Both x values have same sign")
    elif f(midpoint) > 0:
        if f(x_2) < 0:
            return bisection_root(f, midpoint, x_2)
        elif f(x_1) < 0:
            return bisection_root(f, midpoint, x_1)
        else:
            raise ValueError("Both x values have same sign")

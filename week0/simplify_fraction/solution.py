def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(a, b-a)
    return gcd(a-b, b)

def simplify_fraction(fraction):
    devisor = gcd(fraction[0],fraction[1])
    return (int(fraction[0] / devisor), int(fraction[1] / devisor))

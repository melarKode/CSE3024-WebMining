from math import log, ceil

log2 = lambda x: log(x, 2)

def unary(x):
    return (x-1)*'0' + '1'

def binary(x, l=1):
    s = '{0:0%db}'%l
    return s.format(x)

def eliasGeneric(lencoding, x):
    if x == 0:
        return '0'
    l = 1+int(log2(x))
    a = x - 2**(int(log2(x)))
    k = int(log2(x))
    return lencoding(l) + binary(a,k)

def golomb(b, x):
    q = int((x) / b)
    r = int((x) % b)
    l = int(ceil(log2(b)))
    return unary(q) + binary(r, l)

def eliasGamma(x):
    return eliasGeneric(unary, x)

def eliasDelta(x):
    return eliasGeneric(eliasGamma,x)

print(eliasGamma(10))
print(eliasDelta(10))
print(golomb(5, 9))
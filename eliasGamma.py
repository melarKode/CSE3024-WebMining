from math import log

log2 = lambda x: log(x, 2)

def unary(x):
    return (x-1)*'0' + '1'

def binary(x, l=1):
    s = '{0:0%db}'%l
    return s.format(x)

def eliasGamma(x):
    if x==0:
        return '0'
    n = 1+int(log2(x))
    b = x-2**int(log2(x))

    l = int(log2(x))

    return unary(x)+binary(x,l)

print(eliasGamma(10))
from pylab import *

def funktion(x):
  return x**3 + x - 28

def ableitung(x):
  return 3*x**2 + 1

checkvalue = 2.6
Value = []
while checkvalue not in Value:
  Value.append(checkvalue)
  checkvalue = checkvalue - (funktion(checkvalue) / ableitung(checkvalue))

print(checkvalue)


'''
pseudo = 0.0000000000000001

def root(roota, rootb):
    xold = 0
    if roota == 0:
        return roota
    if (rootb > roota):
        xold = rootb
    else:
        xold = roota
    xnew = 0
    checkvalue = 0
    if (rootb < 0):
        rootb *= -1
    if roota != 2:
        while pseudo < checkvalue:
            xnew = (1/roota) * ((roota-1) * xold + (rootb/(xold ** roota-1)))
            checkvalue = xold - xnew
            xold = xnew
    else:
        while pseudo < checkvalue:
            xnew = 0.5 * (xold + (rootb/xold))
            checkvalue = xold - xnew
            xold = xnew
    return xnew

print(root(16,2))
'''






























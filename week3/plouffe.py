from sympy import Rational

pi = 0
for i in range(0,633):
  pi += Rational(1,16**i)*(Rational(4,8*i+1)-Rational(2,8*i+4)-Rational(1,8*i+5)-Rational(1,8*i+6))


print (pi.evalf(769))


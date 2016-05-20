from sympy import Rational

def arctan(x):
    left_sum = 0
    right_sum = 0
    for i in range(1,1096,4):
        left_sum += x**i/i
    for i in range(3,1096,4):
        right_sum += x**i/i
    return left_sum-right_sum

pi = 16 * arctan(Rational(1,5)) - 4*arctan(Rational(1,239))
print(pi.evalf(769))




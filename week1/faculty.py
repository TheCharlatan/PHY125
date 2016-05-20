from pylab import *
from sympy import Rational

def fak(n):
  if n == 1 or n == 0:
    return 1
  return n*fak(n-1)

print (fak(9))

main_list = []
main_list.append(1);

def Bernoulli(n):
    B_n = 0
    sum_holder = 0
    for i in range(0, n-1):
        #Berechne das naechste Element in der Liste
        for k in range (0, i+1):
            sum_holder += Rational(1,1)*(fak(i+1) * main_list[k]) / (fak(k) * fak(i+1-k+1))

        main_list.append(sum_holder*-1)

        #Berechne den naechsten Summenterm
        B_n += Rational(1,1)*(fak(n) * main_list[n-1]) / (fak(i) * fak(n-i+1))
    return -B_n



print(Bernoulli(500))








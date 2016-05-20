from pylab import *
#from sympy import Rational
import time


#def fak(n):
#  if n == 1 or n == 0:
#    return 1
#  return n*fak(n-1)

def fak(n):
    f = 1
    while (n > 0):
        f = f * n
        n = n - 1
    return f


main_list = []
main_list.append(1)

def Bernoulli(n):
    B_n = 0
    #main_list = [0] * n
    #main_list[0] = 1
    for i in range(0, n):
        sum_holder = 0
        #Berechne das naechste Element in der Liste und füge es hinzu
        if i < n-1:
            if i % 2 == 1 or i == 0:
                for k in range (0, i+1):
                    if k%2 == 0 or k == 1:
                        sum_holder += (fak(i+1) * main_list[k]) / (fak(k) * fak(i+1-k+1))
                #main_list[i+1] = sum_holder*-1
                main_list.append(sum_holder*-1)
            else:
                main_list.append(0)
            #else:
                #main_list[i] = 0

        #Berechne den naechsten Summenterm
        if i%2 == 0 or i == 1:
            B_n += (fak(n) * main_list[i]) / (fak(i) * fak(n-i+1))
    return -B_n


startTime = time.time()
print(Bernoulli(8))

print("Took %s seconds" % (time.time() - startTime))








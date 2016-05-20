from pylab import *
import math

epsilon = 0
counter = 0

exponent = range(1,1000)
big_array = []
for i in exponent:
    big_array.append(10**i)

#Check for smallest epsilon
for i in big_array:
    epsilon = 1/i
    if ((1 + epsilon) == 1):
        break;
print(epsilon)

#Check for smallest epsilon/2
for i in big_array:
    epsilon = 1/i
    counter += 1
    if ((epsilon/2)== 0):
        break;

print(counter)
print(epsilon)
counter = 0


exponent = 2
basis = 2
growing = 2
while (growing+1.0) != growing:
  growing = basis ** exponent
  exponent += 1

print(counter)
print(exponent-1)



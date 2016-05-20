#author: sebkue
#Sebastian Kung

from pylab import *

def ist_prime(tester):
  if (tester % 2 == 0):
    return 0
  else:
    parser = 2
  # while parser < tester/2:
    while parser * parser < tester:
      parser+=1
      if tester % parser == 0:
        return 0
    return 1

position = 1
number = 3
while position < 10001:
  number += 1
  if ist_prime(number):
    position+=1
    print(position, number)
    number+=1

print (number)























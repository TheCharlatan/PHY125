from pylab import *
from scipy.stats import norm
import random

def pascal(n):
  """Calculates the full Pascal triangle
  n: Integer
     How many levels of the triangle are supposed to be calculated"""
  #Initialise the main Pascal Triangle
  PascalTri = list((n+1)*[[1]])

  for i in range(n):
    PrevRow = PascalTri[i]
    NewRow = list([1])
    for j in range(len(PrevRow)):
      if j+1 == len(PrevRow):
        NewRow.append(1)
      else:
        NewRow.append(PrevRow[j]+PrevRow[j+1])
    PascalTri[i+1] = NewRow
  return PascalTri


def blank_triangle(n):
  """Gives Pascal's triangle with all zeros.
  n: Integer
     Levels of the triiangle to be computed"""
  PascalTri = list((n+1)*[[0]])
  for i in range(n):
    PrevRow = PascalTri[i]
    NewRow = list([0])
    for j in range(len(PrevRow)):
      if j+1 == len(PrevRow):
        NewRow.append(0)
      else:
        NewRow.append(0)
    PascalTri[i+1] = NewRow
  return PascalTri


def random_walk(n, triangle):
  """Fills a triangle with random walk results.
  n: Integer
    Number of walks made"""
  for i in range(0, n):
    position = 0
    for j in range(1, len(triangle)):
      choices = [position, position+1]
      choice = random.choice(choices)
      position = choice
    triangle[len(triangle)-1][position] += 1
  return triangle



def pascal_gauss(level, x=None):
  """ Calculates the gaussian values corresponding to Pascal's trinagle
  Parameters
  ----------
  level : int
  level of pascals triangle to calculate values for
  x : array of floats or ints
  positions where the gaussian distribution should be evaluated
  default: positios in Pascal's Trinagle, numbered as 0, 1, ...
  Returns
  -------
  values : array of floats
  values corresponding to the given Positions
  Examples
  --------
  >>> pascal_gauss(1) # compare to [1, 1] from Pascal's Trinagle
  array([ 0.9678829,  0.9678829])
  >>> pascal_gauss(1, frange(-0.5, 1.5, 0.5)) # useful for plotting
  array([ 0.21596387,  0.9678829 ,  1.59576912,  0.9678829 ,  0.21596387])
  """
  if x is None:
    x = range(level+1)
    # norm.pdf(positions, mean, standard_deviation)
  return 2**level*norm.pdf(x, level/2,  sqrt(level/4))


depth = 20
pascal_triangle = pascal(depth)
pascal_gauss = pascal_gauss(depth)
random_triangle = blank_triangle(depth)
walk = random_walk(10000, random_triangle)

print(walk[-1])
print(pascal_triangle[-1])
print(pascal_gauss)

plot(pascal_triangle[-1], color='y')
plot(pascal_gauss, color='b')
plot(walk[-1], color='r')
show()




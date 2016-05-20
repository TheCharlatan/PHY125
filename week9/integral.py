from pylab import *


def riemann_integrate(f, lower, upper, depth):
  x = linspace(lower, upper, depth)
  fx = f(x)
  width = (upper-lower) / depth
  rectangles = fx * width
  area = sum(rectangles[:-1])
  return area

def simpson_integrate(f, lower, upper, depth):
  x = linspace(lower, upper, depth)
  width = (upper-lower) / depth
  rectangles = 1/3 * (width/2) * f(x) + 4/3 * (width/2) * f((2*x+width)/2) + 1/3 * (width/2) * f(x+width)
  area = sum(rectangles[:-1])
  return area

def precise_integrate(f, lower, upper, depth):
  x = linspace(lower,upper, depth)
  width = (upper-lower) / depth
  rectangles = 3/2 * (width/6 * f((2*x+width)/2)) + 9/4 * (width/6 * f((6*x+width)/6) + width/6 * f((6*x+5*width)/6))
  area = sum(rectangles[:-1])
  return area



depth = 1000
print("First the results of Riemann Integration")
integral = riemann_integrate(sin, 0, pi, depth)
print(integral)
integral = riemann_integrate(cos, 0, pi, depth)
print(integral)

print("Now follows the Simpson Integration:")
integral = simpson_integrate(sin, 0, pi, depth)
print(integral)
integral = simpson_integrate(cos, 0, pi, depth)
print(integral)

print("Now follows the Improved Simpson Integration:")
integral = precise_integrate(sin, 0, pi, depth)
print(integral)
integral = precise_integrate(cos, 0, pi, depth)
print(integral)

def f(x):
  return log(sin(x))

print("Assignment numeric integration test with int_0^pi/2 ln(sin(x)) dx:")
integral = precise_integrate(f, 0, pi/2, depth)
actual = -pi/2 * log(2)
print(integral)
print("The actual result is:", actual)





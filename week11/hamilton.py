from pylab import *

x0=array([13,0.5,1,5])
t=linspace(0,10,555)
w=0.5
ep=2


lx2=[]

def F(X,t):
  return array([-sin(X[2])-ep*sin(X[2]-X[3]),ep*sin(X[2]-X[3]),X[0],w])


def runge2(F,x0,t):
  x = x0
  dt = t[2]-t[1]
  for i in t:
      x= x + dt * (1/2) * (F(x,t) + F(x+dt * F(x,t), t))
      lx2.append(x)


runge2(F,x0,t)


p=[x0[0]]
P=[x0[1]]
q=[x0[2]]
Q=[x0[3]]

for i in lx2:
  p.append(i[0])
  P.append(i[1])
  q.append(i[2])
  Q.append(i[3])

H=[]

for i in range(len(t)):
  h=1/2*p[i]**2+w*P[i]-cos(q[i])-ep*cos(q[i]-Q[i])
  H.append(h)

plot(t,H,'oc')
axis([-1,12,80,90])
show()

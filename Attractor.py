import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

s,r,b=1,1,1 #parameters

def dLorenz(XYZo,t): #ODE system
  x,y,z=XYZo
  return [s*y-s*x,r*x-x*z-y,x*y-b*z]

XYZo=[0,1,0] #initial condition

t = np.linspace(0, 3, 10001) #tspace

sol = odeint(dLorenz, XYZo, t) #solver

fig=plt.figure() #plot
plt.plot(t, sol[:, 0], 'r', label='x(t)')
plt.plot(t, sol[:, 1], 'g', label='y(t)')
plt.plot(t, sol[:, 2], 'b', label='z(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
fig.savefig("plot.png")

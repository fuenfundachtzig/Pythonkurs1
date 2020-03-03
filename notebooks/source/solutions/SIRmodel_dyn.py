# 
# solution for SIR model with vital dynamics
# 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def F(y, t, c, w, b, d):
  "return the derivates defining the differential equations of the SIR model, y = (S, I, R)"
  N = sum(y)
  S, I, R = y
  dS = -c*S/N*I      + b*N - d*S
  dI =  c*S/N*I -w*I       - d*I
  dR =           w*I       - d*R
  return dS, dI, dR


# time steps [assume days as time unit]
t_min = 0
t_max = 300
dt    = 1
t     = np.arange(t_min, t_max+dt, dt)

# initial conditions and constants
y0 = (1000., 1., 0.) # (note: we use floats although individual counts are integers)
c  = 0.15
w  = 0.05

# new: birth and death rate 
# (b = d => N = const.)
# (these rates are usually much smaller than c and w)
b  = 0.001
d  = 0.001

# solve system of ODEs
S, I, R = odeint(F, y0, t, args = (c, w, b, d)).T

# plot result
plt.plot(S, label = "susceptible")
plt.plot(I, label = "infected")
plt.plot(R, label = "recovered")
plt.plot(S+I+R, label = "total")
plt.xlabel("time [days]")
plt.ylabel("individuals [1]")
plt.legend()

# show plot
plt.ion()
plt.show()


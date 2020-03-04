# 
# solution for SIR model
# 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def F(y, t, N, c, w):
  "return the derivates defining the differential equations of the SIR model, y = (S, I, R)"
  S, I, R = y
  dS = -c*S/N*I
  dI =  c*S/N*I -w*I
  dR =           w*I
  return dS, dI, dR


# time steps [assume days as time unit]
t_min = 0
t_max = 300
dt    = 1
t     = np.arange(t_min, t_max+dt, dt)

# initial conditions and constants
y0 = (1000., 1., 0.) # (note: we use floats although individual counts are integers)
N  = sum(y0)
c  = 0.15
w  = 0.05
print("r =", c/w, "(basic reproduction number)")
if c/w > N/y0[0]:
  print("Outbreak")

# solve system of ODEs
S, I, R = odeint(F, y0, t, args = (N, c, w)).T

# plot result
plt.plot(S, label = "susceptible")
plt.plot(I, label = "infected")
plt.plot(R, label = "recovered")
plt.xlabel("time [days]")
plt.ylabel("individuals [1]")
plt.legend()

# show plot
plt.ion()
plt.show()


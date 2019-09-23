# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
import scipy as sp
from scipy.integrate import odeint
#import matplotlib.pyplot as plt
R1=8
R2=3
L1=1 
L2=1
def RLC(I,t):
    di2_t=(R2/L1)*I[0] - (R2/L1)*I[1]  
    di1_t=(-(R1+R2)/L2)*I[0] + (R2/L2)*I[1] + (100*np.sin(t))/L2 + di2_t
    return di1_t, di2_t
i0 = 0,0
t = np.linspace(0,2,100)
sol=odeint(RLC, i0, t)
plt.plot(t, sol[:, 0], label="i1_t")
plt.plot(t, sol[:, 1], label="i2_t")
plt.legend()
plt.show()
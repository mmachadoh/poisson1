# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:59:31 2019

@author: mmachadoh
"""
import numpy as np
import scipy as sp
import sympy as sympy
import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt
import math
#
from scipy.integrate import odeint
from scipy.integrate import ode
from numpy import linalg as la
from scipy.integrate import quad
#
# Resolviendo ecuación diferencial
# Definimos el sistema de ecuaciones
def f(xyz, t, sigma, rho, beta):
    x, y, z = xyz
    return [sigma * (y - x), 
           x * (rho - z) - y,
           x * y - beta * z]

# Asignamos valores a los parámetros
sigma, rho, beta = 8, 28, 8/3.0

# Condición inicial y valores de t sobre los que calcular
xyz0 = [1.0, 1.0, 1.0]
t = np.linspace(0, 25, 10000)

# Resolvemos las ecuaciones
xyz1 = integrate.odeint(f, xyz0, t, args=(sigma, rho, beta))
xyz2 = integrate.odeint(f, xyz0, t, args=(sigma, rho, 0.6*beta))
xyz3 = integrate.odeint(f, xyz0, t, args=(2*sigma, rho, 0.6*beta))
#

# Graficamos las soluciones
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig, (ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(12, 4),
                                  subplot_kw={'projection':'3d'})

for ax, xyz, c in [(ax1, xyz1, 'r'), (ax2, xyz2, 'b'), (ax3, xyz3, 'g')]:
    ax.plot(xyz[:,0], xyz[:,1], xyz[:,2], c, alpha=0.5)
    ax.set_xlabel('$x$', fontsize=16)
    ax.set_ylabel('$y$', fontsize=16)
    ax.set_zlabel('$z$', fontsize=16)
    ax.set_xticks([-15, 0, 15])
    ax.set_yticks([-20, 0, 20])
    ax.set_zticks([0, 20, 40])
## SEGUNDO EJEMPLO
# CIRCUITO
R1=8
R2=3
L1=1 
L2=1 

def RLC(I,t):
    i1, i2 = I
    di2_t=(R2/L1)*i1 - (R2/L1)*i2  
    di1_t=(-(R1+R2)/L2)*i1 + (R2/L2)*i2 + (100*np.sin(t))/L2 + di2_t
    return di1_t, di2_t

i0 = 0,0

t = np.linspace(0,2,100)

sol=odeint(RLC, i0, t)
plt.plot(t, sol[:, 0], label="i1_t")
plt.plot(t, sol[:, 1], label="i2_t")
plt.legend()
plt.show()

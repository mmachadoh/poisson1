# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:59:31 2019

@author: mmachadoh
"""
import numpy as np
import scipy as sp
import sympy as sympy
from scipy.integrate import odeint
#from scipy.integrate import ode
import matplotlib.pyplot as plt
from numpy import linalg as la
import math  
#
# Resolviendo ecuación diferencial
# f(x, y(x)) = x + y(x)^2
# Defino la función
f = y(x)**2 + x
f
# Defino la función
# la convierto en una función ejecutable
f_np = sympy.lambdify((y(x), x), f)

# Definimos los valores de la condición inicial y el rango de x sobre los 
# que vamos a iterar para calcular y(x)
y0 = 0
xp = np.linspace(0, 1.9, 100)

# Calculando la solución numerica para los valores de y0 y xp
yp = integrate.odeint(f_np, y0, xp)

# Aplicamos el mismo procedimiento para valores de x negativos
xn = np.linspace(0, -5, 100)
yn = integrate.odeint(f_np, y0, xn)
#
#
## campo de direcciones
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
plot_direction_field(x, y(x), f, ax=axes)
axes.plot(xn, yn, 'b', lw=2)
axes.plot(xp, yp, 'r', lw=2)
plt.show()

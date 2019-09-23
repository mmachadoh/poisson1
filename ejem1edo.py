# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:59:31 2019

@author: mmachadoh
"""
import numpy as np
import scipy as sp
import sympy as sympy
from scipy.integrate import odeint
# Resolviendo ecuación diferencial
# \frac{dy}{dx} = -3x^2y + 6x^2
# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')
### expreso la ecuacion
f = 6*x**2 - 3*x**2*(y(x))
sympy.Eq(y(x).diff(x), f)
#
## Resolviendo la ecuación
print(sympy.dsolve(y(x).diff(x) - f))




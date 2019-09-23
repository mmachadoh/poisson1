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
from scipy.integrate import solve_ivp
#
# Resolviendo ecuación diferencial

def exponential_decay(t, y): return -0.5 * y
sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])
print(sol.t)
#
# Especificar puntos donde se desea la solución.
print(sol.t)
print(sol.y)

## otro ejemplo de EDO


# %% Imports






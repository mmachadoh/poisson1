# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:59:31 2019

@author: mmachadoh
"""
import numpy as np
import scipy as sp
import sympy as sympy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#
# Resolviendo ecuación diferencial
# \frac{dy}{dx} = -3x^2y + 6x^2
# Defino incognitas
x = sympy.symbols('x')
y = sympy.Function('y')
# Defino la función
f = y(x)**2 + x**2 -1
#
# grafico de campo de dirección
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
campo_dir = plot_direction_field(x, y(x), f, ax=axes)


# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:13:43 2019

@author: mmachadoh
"""
import numpy as np
from sympy import *
# Use ODEINT to solve the differential equations defined by the vector field
from scipy.integrate import odeint

#     Defines the differential equations for the coupled AMOCO system.
#def vectorfield(w, t, p):
#    """
#    Arguments:
#        w :  vector of the state variables:
#                  w = [x1,s1,x2,s2,A,C]
#        t :  time
#        p :  vector of the parameters:
#                  p = [alf,a1,a2,D,m1,m2,ks1,ks2,ki2,k1,k2,k3,k4,k5,k6,Kla,kH,PT,S1in,S2in,Ain,Cin]
#    """
# Parameter values
m1=1.2
ks1 = 7.1 # Half saturation constant for acetate degradation
alf = 0.5
D = 0.3857
S1in = 2
m2 = 0.82 #% Monod maximun specific growth rate
k1 = 30.54 #% Yield for substrate degradation
k2 = 115.05 #% Yield for substrate degradation
k3 = 160.155
ks2 = 9.28 #% Half saturation constant for acetate degradation
ki2 = 256
S2in = 87.5
Ain = 87.5
Cin = 87.5
k4 = 97.1
k5 = 209.7
kla = 19.8
kH=16
PT=0.037
       
# Initial condition
x1=1.25
s1=2.5
x2=1.25
s2=10
A=90
C=90
# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250
# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]
# Pack up the parameters and initial conditions:
w0= [x1, s1, x2, s2, A, C]
p = [alf, a1, a2, D, m1, m2, ks1, ks2, ki2, k1, k2, k3, k4, k5, k6, Kla, kH, PT, S1in, S2in, Ain, Cin]
import math
    # Create f = (x1',s1',x2',s2',A',C'):
f = [((m1*s1)/(s1+ks1))-alf*D)*x1,
     D*(S1in-s1)-k1*(m1*s1)/(s1+ks1)*x1,
     (((m2*ki2*s2)/((s2*s2)+ki2*s2+ki2*ks2))-alf*D)*x2,
     D*(S2in-s2)+k2*((m1*s1)/(s1+ks1))*x1-k3*((m2*ki2*s2)/((s2*s2)+ki2*s2+ki2*ks2))*x2,
     D*(Ain-A),
     D*(Cin-C)+k4*((m1*s1)/(s1+ks1))*x1+k5*((m2*ki2*s2)/((s2*s2)+ki2*s2+ki2*ks2 ))*x2-(Kla*(C+s2-A-(((C+s2-A+kH*PT+(k6/Kla)*((m2*ki2*s2)/((s2*s2)+ki2*s2+ki2*ks2))*x2)/(2*kH))+((math.sqrt(((C+s2-A+kH*PT+(k6/Kla)*((m2*ki2*s2)/((s2*s2)+ki2*s2+ki2*ks2))*x2)**2)-4*kH*PT(C+s2-A)))/(2*kH))))]
     return f
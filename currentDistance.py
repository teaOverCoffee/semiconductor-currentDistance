import sys
import os
import math

# assuming an intrinsic semiconductor

pi = 3.1415926
h_cross = 6.626*(10**(-34))/(2*pi)
me = 9.11*(10**(-31))
me = 9.11*(10**(-31))
Eg = 1.1*1.6*(10**(-19))
Ev = 0
Ec = Eg
Ei = ((Ev+Ec)/2) + (3/4)*k*T*math.log(mp/me)
Ef = Ei
k = 1.38*math.pow(10, -23)
T = 300

Nc = 2*math.pow(((2*pi*me*k*T)/(h_cross**2)),1.5)
Nv = 2*math.pow(((2*pi*mh*k*T)/(h_cross**2)),1.5)

ni = math.sqrt(Nc*Nv*math.expm1(-Eg/(k*T)))

n = Nc*math.expm1((Ef-Ec)/(k*T))
p = Nv*math.expm1((Ev-Ef)/(k*T))


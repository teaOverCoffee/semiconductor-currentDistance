import sys
import os
import math
import matplotlib.pyplot as plt

# assuming an intrinsic Silicon semiconductor
# net current, I = I(diode, saturation) - I(photocurrent)

pi = 3.1415926
h_cross = 6.626*(10**(-34))/(2*pi)
me0 = 9.11*(10**(-31))
mp0 = 9.11*(10**(-31))

tauN = 10**(-7)
tauP = 10**(-7)
Dn = 30*(10**(-4))
Dp = 15*(10**(-4))

Ln = math.sqrt(Dn*tauN)
Lp = math.sqrt(Dp*tauP)

q = 1.602*(10**(-19))
k = 1.38*math.pow(10, -23)
T = 300

Eg = 1.1*1.6*(10**(-19))
Ev = 0
Ec = Eg
Ei = ((Ev+Ec)/2) + (3/4)*k*T*math.log(mp0/me0)
Ef = Ei


NA = 10**(18)
ND = 10**(18)

def carrierParameters(altitude):

	if (altitude >= 1 or altitude <= 10**6):
		T = 300 - 200*(10**(-6))*(altitude - 1)
		I = 1300 + 400*(10**(-6))*(altitude - 1)
		me = me0*math.pow(1.000001,1)
		mp = mp0*math.pow(1.000001,1)
	elif (altitude > 10**6 or altitude <= 10**10):
		T = 100 - 98*(10**(-4))*(altitude - 10**6)
		I = 1700 + 300*(10**(-4))*(altitude - 10**6)
		me = me0*math.pow(1.0001,1)
		mp = mp0*math.pow(1.0001,1)

	Nc = 2*math.pow(((2*pi*me*k*T)/(h_cross**2)),1.5)
	Nv = 2*math.pow(((2*pi*mp*k*T)/(h_cross**2)),1.5)

	ni = math.sqrt(Nc*Nv*math.exp(-Eg/(k*T)))

	n = Nc*math.expm1((Ef-Ec)/(k*T))
	p = Nv*math.expm1((Ev-Ef)/(k*T))
	
	return [Nc, Nv, ni, n, p, T, I]

carrierParameters = carrierParameters(1)

Nc = carrierParameters[0]
Nv = carrierParameters[1]
ni = carrierParameters[2]
n = carrierParameters[3]
p = carrierParameters[4]

startHeight = 1
endHeight = 1*(10**8)
step = 100
intervalStep = step

step1 = [step]

V = 0.7
Voc = (k*T/q)*math.log(NA*ND/ni**2)
iSatDark = ni*ni*q*((Dn/(Ln*NA)) + (Dp/(Lp*ND)))
i_dark = [iSatDark*(math.expm1(q*V/(k*T)) - 1)]
i_photo = [iSatDark*(math.expm1(q*Voc/(k*T)) - 1)]

fig = plt.figure()

while (step <= endHeight):
	step += intervalStep
	step1.append(step)
	if(math.ceil(math.log10(step)) == math.log10(step)):
		intervalStep *= 10
		intervalStep = step
	CP = carrierParameters(step)
	ni = CP[2]
	T = CP[5]
	I = CP[6]
	Voc = (k*T/q)*math.log(NA*ND/ni**2)
	iSatDark = ni*ni*q*((Dn/(Ln*NA)) + (Dp/(Lp*ND)))
	i_dark.append(iSatDark*(math.expm1(q*V/(k*T)) - 1))
	i_photo.append(iSatDark*(math.expm1(q*Voc/(k*T)) - 1))
	i = i_dark - i_photo

ax = fig.add_subplot(111)
p = ax.plot(step1, i, 'b')
ax.set_xlabel('x-points')
ax.set_ylabel('y-points')
ax.set_title('Simple XY point plot')
fig.show()
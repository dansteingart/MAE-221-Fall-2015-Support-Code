from pithy import *

"""As shown in Fig. P3.21 0.1 kg of water is contained within a piston-cylinder assembly at 100 C. The piston is free to move smoothly in the cylinder. The local atmospheric pressure and acceleration of gravity are 100 kPa and 9.81 m/s2, respectively. For the water, determine the pressure, in kPa, and volume, in cm3.
"""

g = 9.81 # m/s^2
m = 50   # kg
A = 0.01 #m^3
P_atm = 1e5
P = m*g/A + P_atm

T = 100 +273 #K
St = {}
m_water = .1
St[1] = stater('P',P,'T',T,'water')
print state_table(St)
print "Total Volume is "+str(m_water*St[1]['V'])[0:10] +"m^3"
#whos(locals())

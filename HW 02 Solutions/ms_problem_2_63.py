from pithy import *

"""As shown in Fig. P2.63, the outer surface of a transistor is cooled convectively by a fan-induced flow of air at a temperature of 25C and a pressure of 1 atm. The transistor's outer surface area is 5x10^-4. At steady state, the electrical power to the transistor is 3 W. Negligible heat  transfer occurs through the base of the transistor. The convective heat transfer coefficient is 100 W/m^2 K.  Determine (a) the rate of heat transfer between the transistor  and the air, in W, and (b) the temperature at the transistor's outer surface, in 8C.
"""


h = 100 #W/m^2 K
T_air = 25 + 273
Area = 5e-4 #m^2

#Part A
Edot = 3
Wdot = 0
Qdot = Wdot-Edot #W
print "Part A) The heat transfer is %s W" % str(Qdot)[0:4]
#Part B
#Qdot  = -hA(T_s-T_air)

Ts = -Qdot/(h*Area) + T_air
print "Part B) The surface temperature of the chip %s C" % str(Ts-273)[0:4]
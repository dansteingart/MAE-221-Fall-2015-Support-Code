from pithy import *

"""The outer surface of the grill hood shown in Fig. P2.55 is  at 478C and the emissivity is 0.93. The heat transfer coefficient for convection between the hood and the surroundings at  278C is 10 W/m^2K. Determine the net rate of heat transfer  between the grill hood and the surroundings by convection and radiation, in kW per m2 of surface area."""



Ts = 47 + 273 #K
Tb = 27 + 273 #K
eps = 0.93 #
h   = 10 # W/m^2
sigma = 5.67E-8 #W/m^2K^4
#Convection
QdotbyA_conv = h*(Ts-Tb)

print "The heat transfer due to convection is %.2e W/m^2" % QdotbyA_conv

#Radiation
QdotbyA_rad = eps*sigma*(Ts**4-Tb**4)
print "The heat transfer due to radiation is %.2e W/m^2" % QdotbyA_rad

#Total
print "The total heat transfer  is %.2e W/m^2" % float(QdotbyA_rad+ QdotbyA_conv)


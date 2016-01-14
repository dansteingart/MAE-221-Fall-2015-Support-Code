from pithy import *

# Air flows through an insulated circular duct having a diameter of 2 cm. Steady-state pressure and temperature data obtained by measurements at two locations, denoted as 1 and 2, are given in the accompanying table. Modeling air as an ideal gas with cp = 1.005 kJ/(kg K), Mair  = 28.97 kg/kmol and R = 8.3144 kJ/(kmol K) determine 
# (a) the entropy balance of the operation
# (b) the direction of the flow (1 to 2 or 2 to one)
# (c) the velocity of the air, in m/s, at each of the two locations, 
# (d) the mass flow rate of the air, in kg/s.

print "A and B) Entropy tells us the Direction of Flow"

cp = 1.005
R = 8.31446
M = 28.97
Rair = R/M

T1 = 20+273.
T2 = 50+273.

P1 = float(1e5)
P2 = 5e5

#sigma_dot_over_m_dot = S2 - S1
sigma_dot_over_m_dot = cp*log(T2/T1) - Rair*log(P2/P1)

print "sigma_dot_over_m_dot = cp*log(T2/T1) + Rair*log(P2/P1) = %.2f kJ/(kg K)" % sigma_dot_over_m_dot

print "The flow must be from location 2 to 1 since from 1 to 2 the entropy change is negative"


print
print "C and D) Now an enthalpy balance to determine the velocity and mass flow rate"

# mdot1 = mdot 2 
# Av1/V1  =  Av2/V2
# Av1*RT1/P1 = # Av2*RT2/P2 
# v2 = v1*(T2/T1)*(P1/P2) 

velocity_ratio = vr = (T2/T1)*(P1/P2) 

print "velocity_ratio = (T2/T1)*(P1/P2) = %.2f " % velocity_ratio 
print "v2 = %.2f v1" % velocity_ratio

#0 = mdot*(h2 - h1 - (delta V)^2/2)
#0 = mdot*(cp*(T2 - T1) - v1^2-(v1*veloocity_ratio)^2/2)

v1 = sqrt(2*cp*(T2-T1)/(1-vr**2)*1000)
print "v1 = sqrt(2*cp*(T2-T1)/(1-vr**2)*1000) = %.2f m/s" % v1 #Nm to kJ
v2 = vr*v1
print "v2 = vr*v1 = %.2f m/s" % v2

A = (0.02/2)**2*3.1415
mdot = A*v1 * P1/(Rair*T1) * (1/1000.) #kJ to Nm
print  "mdot = %.3f kg/s" % mdot






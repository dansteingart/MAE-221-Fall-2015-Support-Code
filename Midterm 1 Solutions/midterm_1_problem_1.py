from pithy import *

R = 8.31446 #kJ/kmol K
M = 28.97 #kJ/kmol

R_air = 1000*R/M  #> Convert to Joule/kg basis

#States
p1 = 5e5 #Pa
v1 = 1   # m^3/kg
T1 = p1*v1/R_air # K
u1 = stater('P',p1,'T',T1,'air')['U']

p2 = 1e5 #Pa
v2 = 5   # m^3/kg
T2 = p2*v2/R_air # K
u2 = u1


p3 = 1e5 #Pa
v3 = 1   # m^3/kg
T3 = p3*v3/R_air # K
u3 = stater('P',p3,'T',T3,'air')['U']


#Processes
U12 = 0 #Isothermal
W12 = R_air*T1*log(v2/v1)
Q12 = U12+W12

U23 = u3-u2
W23 = p2*(v3-v2)
Q23 = U23+W23

U31 = u1-u3
W31 = 0
Q31 = U31+W31


out = "Steps,U(kJ/kg),W(kJ/kg),Q(kJ/kg)\n"
out += "1-2,%.2f,%.2f,%.2f\n" % (U12/1000,W12/1000,Q12/1000)
out += "2-3,%.2f,%.2f,%.2f\n" % (U23/1000,W23/1000,Q23/1000)
out += "3-1,%.2f,%.2f,%.2f\n" % (U31/1000,W31/1000,Q31/1000)

print csv_to_table(out)

eta = (W12+W23)/(Q12+Q31)

print "The Thermal Efficiency is ", round(eta*100,2),"%"


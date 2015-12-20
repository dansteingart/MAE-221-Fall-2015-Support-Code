from pithy import *

T1 =  300.0 #K
T2 =  862.4 #K
T3 = 1800.0 #K
T4 = 1980.0 #K
T5 =  840.3 #K

u1 = 214.07 #kJ/kg 
u2 = 643.35 #kJ/kg
u3 = 1487.2 #kJ/kg
u4 = 1659.5 #kJ/kg
u5 = 625.19 #kJ/kg

h1 =  300.19 #kJ/kg 
h2 =  890.89 #kJ/kg
h3 = 2003.30 #kJ/kg
h4 = 2227.10 #kJ/kg
h5 =  866.41 #kJ/kg

P1 =   95.0 # kPa
P2 = 4372.8 # kPa
P3 = 9126.9 # kPa
P4 = P3     # kPa
P5 =  265.7 # kPa

mair = 0.05 #kg
Rair = 8.31446 / 28.97 #kJ/(kg K)

V1 = mair * Rair * T1/(P1*1e3)
V2 = mair * Rair * T2/(P2*1e3)
V3 = mair * Rair * T3/(P3*1e3)
V4 = mair * Rair * T4/(P4*1e3)
V5 = mair * Rair * T5/(P5*1e3)

print "Part a) cut off ratio"
rc = V4/V3
print "rc = %.2f" % rc


print "Part b/c) Find Qin and Qout"
Qin  = mair*((u3-u2)+(h4-h3))
Qout = mair*(u5-u1)

print "Via Table: Heat addition  = %.2f kJ" % Qin
print "Via Table: Heat rejection = %.2f kJ" % Qout
print 
print "Part d) Find net work"

Wnet  = Qin - Qout
print "Via Table: Net Work  = %.2f kJ" % Wnet
print

print "Part e) Find the thermal efficiency"

eta = 1 - (Qout)/(Qin)
print "eta using tables = %.2f" % eta




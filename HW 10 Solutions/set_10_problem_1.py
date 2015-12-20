from pithy import *

T1 = 305.0 #K
T2 = 367.4 #K
T3 = 960.0 #K
T4 = 458.7 #K

u1 = 217.67 #kJ/(kg) 
u2 = 486.77 #kJ/(kg)
u3 = 725.02 #kJ/(kg)
u4 = 329.01 #kJ/(kg)

P1 =  85.0 # kPa
P2 = 767.9 # kPa
P3 =2006.0 # kPa
P4 = 329.1 # kPa

mair = 0.002 #kg
Rair = 8.31446 / 28.97 #kJ/(kg K)
cv = .717 #kJ/(kg K)

print "Part a) Find Qin and Qout"

Qin  = mair*(u3-u2)
Qout = mair*(u4-u1)

print "Via Table: Heat addition  = %.2f kJ" % Qin
print "Via Table: Heat rejection = %.2f kJ" % Qout

Qin  = mair*cv*(T3-T2) 
Qout = mair*cv*(T4-T1)

print "Via cold air standard: Heat addition  = %.2f kJ" % Qin
print "Via cold air standard: Heat rejection = %.2f kJ" % Qout
print 
print "Part b) Find net work"

Wnet_table  = mair*((u3-u2)-(u4-u1))
print "Via Table: Net Work  = %.2f kJ" % Wnet_table

Wnet_cas  = mair*cv*((T3-T2)-(T4-T1))
print "Via cold air standard: Net Work  = %.2f kJ" % Wnet_cas
print

print "Part c) Find the thermal efficiency"

eta = 1 - (u4-u1)/(u3-u2)
print "eta using tables = %.2f" % eta

eta = 1 - (T4-T1)/(T3-T2)
print "eta using cold air standard = %.2f" % eta
print

print "Part d) Find the mean effective pressure"
#Vmax = v@state 1
#PV = mRT
V1 = mair * Rair * T1/(P1*1e3)

#Compression ratio = V2/V1
V2 = mair * Rair * T2/(P2*1e3)


mep_table = Wnet_table/(V1*(1-V2/V1)) 
print "via table: MEP = %.2f kPa" % (mep_table/1000)

mep_cas = Wnet_cas/(V1*(1-V2/V1))
print "via cold air standard: MEP = %.2f kPa" % (mep_cas/1000)

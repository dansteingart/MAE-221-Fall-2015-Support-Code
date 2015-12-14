from pithy import *

#Using air standard "cold" analysis, see comparison in MS 8e pg. 517 

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)

r = 8.0 #compression ratio

TC = 540 * .55 # K
TH = 3600 * .55 # K

#1 to 2, Isentropic Compression

# Delta S = 0 = cv*ln(T2/T1) + R_air ln (V2/V1) 
# Delta S = 0 = cv*ln(T2/T1) + R_air ln (1/8) 
# 0 = cv*ln(T2/T1) + R_air ln (1/8.) 
# cv*ln(T2/T1) = - R_air ln (1/8.)
T1 = TC
P1 = 1e5
V1 = 0.0005663369 # m^3


T2 = T1*exp(-(R_air/cv)*log(1/8.))
P2 = T2/T1 *(r)


#2 to 3, cv heating
T3 = TH
P3 = P2*T3/T2 


#3 to 4, isentropic expansion
T4 = T3*exp(-(R_air/cv)*log(8/1.))
P4 = (T4/T3)*(r)
Q41 = cv*(T4-T1)
Q23 = cv*(T3-T2)

eta = 1 - (Q41/Q23)

print "Eta = %.2f" % eta
print

print "T(K),P(Pa)"
print "%.2f,%.2f" % (T1,P1)
print "%.2f,%.2f" % (T2,P2)
print "%.2f,%.2f" % (T3,P3)
print "%.2f,%.2f" % (T4,P4)
print 


print "Find Mean Effective Pressure"
mass = P1*V1/(R_air*T1)

Wcycle = mass*(Q23-Q41)

mep = Wcycle/(V1*(1-(1/r))) 

print "mep = %.2f bar" % (mep/1e5)

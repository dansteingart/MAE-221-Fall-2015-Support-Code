from pithy import *

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv + R_air

r = 18.  #V1/V2
rc = 2.  #V3/V2, cut off ratio or when fuel addition "cuts off"

T1 = 300 #K
P1 = 1e5 #Pa

#1 to 2, Isentropic Compression

# Delta S = 0 = cv*ln(T2/T1) + R_air ln (V2/V1) 
# Delta S = 0 = cv*ln(T2/T1) + R_air ln (1/8) 
# 0 = cv*ln(T2/T1) + R_air ln (1/8.) 
# cv*ln(T2/T1) = - R_air ln (1/8.)
T2 = T1*exp(-(R_air/cv)*log(1/r))
P2 = P1*(T2/T1 *(r))

# 2 to 3, constant pressure heating
# P2T2/V2 = P3T3/V3
P3 = P2
T3 = T2*rc

#3 to 4, Isentropic Expansion
#T4/T3 = (V3/V4)^(k-1) = (rc/r)^(k-1)
T4 = T3*(rc/r)**(k-1)
#V4 = V1, so P4/T4 = P1/T1
P4 = P1*T4/T1

print "T (K) ,P (Pa)"
print "%.2f,%.2e" % (T1,P1)
print "%.2f,%.2e" % (T2,P2)
print "%.2f,%.2e" % (T3,P3)
print "%.2f,%.2e" % (T4,P4)

Q_C = cv*(T4-T1)
Q_H = cp*(T3-T2)

eta = 1 - Q_C/Q_H
print "eta = %.2f" % eta

W_cycle = Q_H - Q_C
print "W_cycle = %.2f kJ/kg" % W_cycle

v1 = R_air*T1/P1 * 1000 
print "v1 = %.2f m^3/kg" % v1

MEP = W_cycle/v1
print "MEP = %.2f kPa" % MEP


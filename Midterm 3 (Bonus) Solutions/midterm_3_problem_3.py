from pithy import *

#The Atkinson cycle is a modification to the air standard Otto cycle where the constant volume heat rejection step is replace with a constant pressure heat rejection step.  See the figure below


#For the both cycles, using cold air standard analysis of air where Mair = 28.97 g/mol and R = 8.31446 J/(mol K), and k = 1.4

# if p1 = 1 Bar, T1 = 300 K, and Q23/m = 2000 kJ/kg

# Determine T, s (vs. state 1), P and v and present a table for both cycles using the second law and sketch/plot the TS diagram for both cycles on the same plot

# (b) Evaluate the ratio of the thermal efficiency of the Atkinson cycle, 1-2-3-4-1, to the thermal efficiency of the Otto cycle, where for the Otto cycle v4' = v1 and for the Atkinson Cycle p4 = p1

# (c) Evaluate the ratio of the mean effective pressure of the Atkinson cycle to the mean effective pressure of the Otto cycle.

print "Part A) compare PV and TS.  PV is already given by the relationship in the cycle, so determining Ts.  The trick is the change on limts on T and S are determined by the exhaust condition"
print
print "It helps to see that "
print "eta = 1 - Qc/Qa"
print "and this is the converse of the diesel cycle, where Q41 = H4 - H1 = Qc for the atkinson cycle"

print "Other than that, apply the analysis from The examples in chapter 9"

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv + R_air


#pick some arbitrary ratio, it will be the same between the two cycles here

r = 8.0 #compression ratio

TC = 295


#1 to 2, Isentropic Compression

# Delta S = 0 = cv*ln(T2/T1) + R_air ln (V2/V1) 
# Delta S = 0 = cv*ln(T2/T1) + R_air ln (1/8) 
# 0 = cv*ln(T2/T1) + R_air ln (1/8.) 
# cv*ln(T2/T1) = - R_air ln (1/8.)
T1 = TC
P1 = 1e5
V1 = 0.001 # m^3 #picked for convinience, or you could have just done the example mass normalised


T2 = T1*exp(-(R_air/cv)*log(1/8.))
P2 = P1*T2/T1 *(r)


#2 to 3, cv heating @ Q23
T3 = T2 + 2000/cv
P3 = P2*T3/T2 

print "for the otto cycle"
#3 to 4, isentropic expansion
T4 = T3*exp(-(R_air/cv)*log(r/1.))
P4 = P3*(T4/T3)*(1/r)
Q41 = cv*(T4-T1)
Q23 = cv*(T3-T2)

eta = 1 - (Q41/Q23)



print "Eta = %.2f" % eta
print

print "T(K),P(Pa)"
print "%.2f,%.2e" % (T1,P1)
print "%.2f,%.2e" % (T2,P2)
print "%.2f,%.2e" % (T3,P3)
print "%.2f,%.2e" % (T4,P4)
print 


print "Find Mean Effective Pressure"
mass = P1*V1/(R_air*T1)

Wcycle = mass*(Q23-Q41)
print "Wcycle = %.2f kJ" % Wcycle

mep = Wcycle/(V1*(1-(1/r))) 

print "mep = %.2f bar" % (mep/1e5)

print 
print "for the atkinson cycle"
#3 to 4, isentropic expansion
P4a = P1
T4a = T3*exp(-(R_air/cp)*log(P3/P4a))

V2 =  R_air*T2/P2
V4a = R_air*T4/P4a
Q41 = cp*(T4a-T1)
Q23 = cv*(T3-T2)

eta = 1 - (Q41/Q23)



print "Eta = %.2f" % eta
print

print "T(K),P(Pa)"
print "%.2f,%.2e" % (T1,P1)
print "%.2f,%.2e" % (T2,P2)
print "%.2f,%.2e" % (T3,P3)
print "%.2f,%.2e" % (T4a,P4a)
print 


print "Find Mean Effective Pressure"
mass = P1*V1/(R_air*T1)

Wcycle = mass*(Q23-Q41)

print "Wcycle = %.2f kJ" % Wcycle

mep = Wcycle/(V4a-V1) 

print "mep = %.2f bar" % (mep/1e5)





from pithy import *

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv + R_air

mdot  = 6 #kg/s

cpr = 10

#tpr = 

#State 1 to 2 - Compression @ eta = 0.8

T1 = 300 #K
P1 = 100e3 #Pa
P7 = P1 #Air exit
P8 = P7

eta_comp = 0.8
eta_turb = 0.8

T2s = T1*(cpr)**((k-1)/k) # = T1*exp(R_air/cp*log(cpr)) 
T2 = T1+(T2s-T1)/eta_comp
P2 = P1*cpr

#State 2 to 3 Regen
P3 = P2
#Find T3 later

#State 3 to 4 combustor
P4 = P3
T4 = 1400 #K

#So we know that the turbine pressure ratios (tpr) are the same, and the overall pressure drop from state 4 to state 7 is 1000 kPa to 100 kPA
#P4 = tpr*(tpr*P7)

tpr = sqrt(P7/P4)

#State 4 to 5 Turbine 1
P5 = tpr*P4
T5s = T4*(P5/P4)**((k-1)/k)
T5 = T4 - (T4-T5s)*eta_turb

#State 5 to 6 combustor 2 (reheat)
T6 = 1400
P6 = P5
#State 6 to 7 Turbine 2
#State 4 to 5 Turbine 1
T7s = T6*(P7/P6)**((k-1)/k)
T7 = T6 - (T6-T7s)*eta_turb

#Now solve for regen (State 3)
eta_regen = .8

#The regenerator effectiveness is the ability of the regenerator to bring T3 up to T7 (i.e. can the exit of the regen before the first combustor reach thermal equilibrium with the second turbine exit?)  

# eta_turbine = (cp*(T3-T2)) / (cp*(T7-T2))

T3 = T2+eta_regen*(T7-T2) #K

#Finally, assuming no thermal losses with the atomosphere, solve for T8 using 

# 0 = h2+h7-h3-h8 
# cp constant, mdot constant, so
# 0 = T2 + T7 - T3 - T8
T8 = T2+T7-T3 #K

#print a prettyish table

Ts = [T1,T2,T3,T4,T5,T6,T7,T8]
Ps = [P1,P2,P3,P4,P5,P6,P7,P8]

print "<table><tr><td>State</td><td style='width:100px'>T (K)</td><td>P (kPa)</td></tr>",
for i in range(len(Ts)):
    print "<tr><td>%i</td><td>%.2f</td><td>%.2f</td></tr>" % (i+1,Ts[i],Ps[i]/1000),
print "</table>"


#Now find rates
print "Part A) Find Thermal Efficiency"
Qdotin = mdot*cp*((T4-T3)+(T6-T5))
print "Qdotin = %.2f kJ/s" % Qdotin

Qdotout = mdot*cp*(T8-T1)
print "Qdotout = %.2f kJ/s" % Qdotout
eta_cycle = 1- Qdotout/Qdotin
print "eta_cycle = %.2f" % eta_cycle

print ""

print "Part B) Find Back Work Ratio"
Wdotcomp = mdot*cp*(T2-T1)
print "Wdotcomp = %.2f kJ/s" % Wdotcomp
Wdotturb1 = mdot*cp*(T4-T5)
print "Wdotturb1 = %.2f kJ/s" % Wdotturb1
Wdotturb2 = mdot*cp*(T6-T7)
print "Wdotturb2 = %.2f kJ/s" % Wdotturb2

bwr = Wdotcomp/(Wdotturb1+Wdotturb2)
print "bwr = %.2f" % bwr
print

print "Part C) Find Net work"
Wdotcycle = Wdotturb1 + Wdotturb2 - Wdotcomp
print "Wdotcycle = %.2f kJ/s (via Work Analysis)" % Wdotcycle
Wdotcycle = Qdotin - Qdotout 
print "Wdotcycle = %.2f kJ/s (via Heat Analysis)" % Wdotcycle

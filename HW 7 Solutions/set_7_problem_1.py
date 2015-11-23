from pithy import *

#Problem 6.36
#Five kg of water contained in a piston-cylinder assembly expand from an initial state where T1 = 400C, p1 = 700 kPa to a final state where T2 = 200 C, p2 = 300 kPa, with no significant effects of kinetic and potential energy. It is claimed that the water undergoes an adiabatic process between these states while developing work. Evaluate this claim.


T1 = 400 + 273 #K
p1 = 700e3 # Pa

T2 = 200 + 273 #K
p2 = 300e3 #Pa

St = {}

m = 5 #kg
Q = 0



St[1] = stater('P',p1,'T',T1,'water')

St[2] = stater('P',p2,'T',T2,'water')

print state_table(St)

Delta_S = Q/T1 + (m*St[2]['S']-m*St[1]['S'])/1000

print "The entropy generated is %.2f kJ/K" % Delta_S

print "Process is impossible because there is no heat transfer and entropy generated is negative"

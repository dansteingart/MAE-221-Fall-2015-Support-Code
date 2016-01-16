from pithy import *

p1 = 18e3 #Pa
T1 = 216. #K
V1 = 265 #m/s
T2 = 250 #K

#its just a nozzle diffuser problem
#m1 = m2
#Qdotcv = Wdotcv = 0
#This is because no work or heat is cross the CV boundary
#Edot = 0 =  mdot((v1^2 - v2^2)/2 + (h1-h2)) 

#Also 1 (m/s)**2 = J/kg

St = {}
#First we need to see what states we have
St[1] = stater('P',p1,'T',T1,'air')
h1 = St[1]['H']
#State 1 Defined

#Enthalpy is a very weak function of Pressure, so assume P2 = P1
St[2] = stater('P',p2,'T',T2,'air')
h2 = St[2]['H']
#State 2 Defined

V2 = sqrt(V1**2+2*(h1-h2))

print "The exit velocity is %.0f m/s" % V2

print state_table(St)

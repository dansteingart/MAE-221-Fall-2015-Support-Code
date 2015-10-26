from pithy import *

"""One kilogram of air in a piston cylinder assembly undergoes two processes in series from an initial state where p1=0.5MPa, T1=227C
Process 1-2: Constant temperature expansion until the volume is twice the initial volume.

Process 2-3: Constant volume heating until the pressure is again 0.5 MPa.

Sketch the two processes in series on a py diagram. Assuming ideal gas behavior, determine (a) the pressure at state 2, in MPa, (b) the temperature at state 3, in C, and for each of the processes (c) the work and heat transfer, each in kJ."""

m = 1e3 #kg

R = 8.31446
M = 28.97 #gmol
n = m/M

p1 = 5e5 #Pa
T1 = 227 + 273. #K

cv_air = 798 #J/kg

#Process 1 
#p1v1 = p2v2
V1 = n*R*T1/p1
#print v1
V2 = 2*V1
p2 = p1*V1/(V2)
T2 = T1

#Process 2
V3 = V2
p3 = 5e5
T3 = p3*V3/(n*R)


W12 = n*R*T1 * log(V2/V1)
Q12 = W12
W23 = 0
Q23 = cv_air*(T3-T2)
print "The pressure at state 2 is",round(p2/1000,2),"kPa"
print "The temperature at state 3 is ",round(T3,2),"K"

print "For each Process:"
out = "Step,Q (kJ),W (kJ)\n"
out+= "%s,%.1f,%.1f\n" %("1-2",Q12/1000,W12/1000)
out+= "%s,%.1f,%.1f\n" %("2-3",Q23/1000,W23/1000)
print csv_to_table(out)

print "Everything Else!" 
whos(locals())

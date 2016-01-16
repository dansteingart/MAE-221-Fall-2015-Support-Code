from pithy import *

"""A piston cylinder assembly fitted with a spring. The cylinder contains water, initially at 1000 F, and the spring is in a vacuum. The piston face, which has an area of 20 in^2, is initially at x1=20in

The water is cooled until the piston face is at x2=16in.

The force exerted by the spring varies linearly with x according to Fspring=kx, where k=200lb/inch. Friction between the piston and cylinder is negligible. For the water, determine

(a) the initial and final pressures, each in psi (b) the amount of water present, in lb. (c) the work, in Btu. (d) the heat transfer, in Btu."""


T1 = 537.778 + 273 #K
A = 0.0129032 # m^2
x1 = 0.508 #m
x2 = 0.406 #m
k = 890*39.3  #lbf/in to N/m
# p = k*x/A
p1 = k*x1/A
p2 = k*x2/A

#To find the amount of water, figure out the specific volume at a state and divide by full volume

St = {}
St[1] = stater('P',p1,'T',T1,'water')
v1 = St[1]['V']
V1 = x1*A
m = V1/v1
v2 = x2*A/m
#Now find the work, integral of Fdx = integral of kxdx
W12 = k*(x2**2-x1**2)/2

#Now Find U's
U1 = St[1]['U']*m
St[2] = stater('P',p2,'D',1/v2,'water')
U2 = St[2]['U']*m
U12 = U2-U1

Q12 = U12 + W12

print state_table(St)

print "Now back to ugly english units"

print "P1 =",round(p1*0.000145038,2),"psi"
print "P2 =",round(p2*0.000145038,2),"psi"
print "m_water =",round(m*2.2,3),"lbs"
print "W =",round(W12*0.000947817,3),"BTU"
print "Q =",round(Q12*0.000947817,3),"BTU"

#whos(locals())
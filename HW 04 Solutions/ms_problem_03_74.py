from pithy import *



#Always for Problem
mass = 1.2 * 1/2.2 #lb to kg

#State 1
P1 = 689475.7
X1 = 1
#Defined!

#State 2
P2 = P1
X2 = 0.75
#Fully Defined


St1 = stater('P',P1,'Q',X1,'ammonia')
St2 = stater('P',P2,'Q',X2,'ammonia')

#State 3
D3 = St2['D']
X3 = 1

#Coolprops doesn't take D and Q, so we hack it
#Make a range of pressures to search
Ps = linspace(P1,1e6,1000)
#Make a range of densities
Ds = pr('D','P',Ps,'Q',1,'ammonia') 
#Compare Density Range to actual Density and take the closest fit
P3 = Ps[abs(Ds-D3).argmin()]
St3 = stater('P',P3,'Q',X3,'ammonia')
#Fully Defined!

# Q - W = delta U

#For Process #1
#Constant Pressure Process
W12 = P2*(St2['V']-St1['V'])
U12 = St2['U'] - St1['U']
Q12 = W12 + U12
print "Q12=",Q12*mass
print "W12=",W12*mass

#For Process #2
W23 = 0 #dV = 0
U23 = St3['U'] - St2['U']
Q23 = W23 + U23
print "Q23=",Q23*mass


# Q12= -165369.22772 J in BTU => -156.7398 BTU
# W12= -17158.4978411 J in BTU => -16.2631 BTU
# Q23= 151209.405552 J in BTU => 143.3189 BTU

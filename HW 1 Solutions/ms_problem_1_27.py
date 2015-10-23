from pithy import *

"""1.27 Three kg of gas in a piston-cylinder assembly undergo a process during which the relationship between pressure and specific volume is pv^(0.5)= constant. The process begins with p1 = 250 kPa and V1 = 1.5 m3 and ends with p2 = 100 kPa. Determine the final specific volume, in m3/kg. Plot the process on a graph of pressure versus specific volume."""

n = .5

#State 1
m1 = 3 #kg
p1 = 250. #kPa
V1 = 1.5 #m^3

#State 2
m2 = m1
p2 = 100. #kPa
V1 = 1.5 #m^3

#Process
#p1v1^n = p2v2^n
#v2 = V2/m1
v1 = V1/m1
v2 = v1 * (p1/p2)**(1/n)
whos(locals())
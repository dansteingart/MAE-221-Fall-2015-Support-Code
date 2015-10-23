from pithy import *

Lmin = 3 #m
Lmax = 3.5 #m
rho = 987.1 #kg/m^3
g = 9.81 #m/s^2
patm = 1e5 #Pa
D = 4 #m
pi = 3.1415

#Part A
pc = patm + rho*g*Lmax 
print "Pressure at Bottom = %.2e Pa" % pc
#Part B
F_atm  = patm*pi*D**2/4 #N
V_cyl  = pi*Lmin*D**2/4 #m^3
V_cone = 1/3.*pi*(Lmax-Lmin)*D**2/4 #m^3
V = V_cyl + V_cone  #m^3
F_water = rho*g*V
F = F_atm+F_water
print "Total Force = %.2e N" % F


print ""
print "Everything Else"
whos(locals())
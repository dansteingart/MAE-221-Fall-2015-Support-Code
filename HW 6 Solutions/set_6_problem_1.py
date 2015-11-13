from pithy import *

#m1 = m2+m3
St = {}
#Find m1, then we know the rest


A1 = 0.2 #m^2
V1 = 30 # m/s
p1 = 5e5 #Pa
T1 = 360 +273 #K
St[1] = stater('P',p1,'T',T1,'water')
rho1 = St[1]['D']

m1 = A1*V1*rho1
m2 = .5 * m1
m3 = m2

print "The mass flow at exit 1 is %.2f kg/s" % m1
print "The mass flow at exits 2 and 3 are each %.2f kg/s" % m2

from pithy import *



T_H = 120.2 + 273
T_C =  16 + 273
gamma_max = T_H/(T_H-T_C)

print "gamma_max = T_H/(T_H-T_C)"
print "The maximum COP is %.2f" % gamma_max

#lookups

h1 = 504.7
h2 = 2706.7
mdot = 0.05

Q_H_dot = mdot*(h2-h1)*1000
W_cv_dot = 35e3

gamma_real = Q_H_dot/W_cv_dot

print "gamma_real = Q_H_dot/W_cv_dot"
print "The real COP is %.2f" % gamma_real

print "This is possible"



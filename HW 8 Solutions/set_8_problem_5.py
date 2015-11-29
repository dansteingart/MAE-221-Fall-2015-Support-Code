from pithy import *

#Problem Statement
#http://steingart.princeton.edu:8004/mae221fall2015/problem_set_08#6


T_H = 20. + 273 #K
T_C =  2. + 273 #K

Q_wall = 16.4 #kW


print "Part A: If using electrical Heat"
print "Q_wall = WIn"
W_elec = Q_wall 
print "The power required is  %.2f kW" % W_elec
print ""

print "Part B: If using a heat pump of cop = 3"
print "W_elec = Q_wall/cop "
cop = 3
W_elec = Q_wall/cop 
print "The power required is  %.2f kW" % W_elec
print

print "Part B: If using a reversible heat pump "
print "W_elec = Q_wall/cop_ideal "
cop_ideal = T_H/(T_H-T_C)
W_elec = Q_wall/cop_ideal 
print "The power required is  %.2f kW" % W_elec


from pithy import *

#Problem Statement
#http://steingart.princeton.edu:8004/mae221fall2015/problem_set_08#5


Q_H = 1050. #kJ
T_H = 525. #K

Q_C = 700. #kJ
T_C = 350. #K


eta_carnot = 1 - T_C/T_H

eta_claimed = 1 - Q_C/Q_H

whos(locals())

print "since eta_carnot = eta_claimed the process is internally reversible"

print "The overall efficiency is %.1f " % (eta_claimed*100),"%"

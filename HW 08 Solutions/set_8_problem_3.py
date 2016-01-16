from pithy import *

#Problem Statement
#http://steingart.princeton.edu:8004/mae221fall2015/problem_set_08#4

St = {}

T1  = 67+273 #K
p1 = 0.95e5 #Pa
vel1 = 75 #m/s
St[1] = stater('P',p1,'T',T1,'air')

T2  = 22+273 #K
p2 = 0.8e5 #Pa
vel2 = 310 #m/s
St[2] = stater('P',p2,'T',T2,'air')

print state_table(St)

#Qdotcv = 0 (insulated duct)
#Wdotcv = 0 (no clear way to get work out)
#PE = 0 (horizontal duct)

#one inlet, one outlet => mass flow rates equal
#What's left is KE and H

# 0 = m1((h1-h2) + (V1^2-V2^2)/2)

print "Whichever state has the higher entropy is the exit"
for i in range(1,3): print "s_%i = %.2f kJ/(kg K)" % (i,St[i]['S']/1000)
print "The air flows from area 2 to area 1"

print 
print  "Using table A-22"

# s2 - s1 = s0(T2) - s0(T1) - R ln(p2/p1)
s20 = 1.686 # kJ/(kg K) 
s10 = 1.827 # kJ/(kg K)
R = (8.314/28.97) # kJ/(kg K)
delS = s20-s10 - R*log(p2/p1)
print "If the flow is from state 1 to 2 then the entropy change is %.2f kJ/(kg K), which is impossible" % delS
print "Overall, the slight delocalization due to pressure increase does not decrease then entropy more than the 45 degree temperature increase from state 2 to 1"
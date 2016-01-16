from pithy import *

#Problem Statement
#http://steingart.princeton.edu:8004/mae221fall2015/problem_set_08#3


#Define The States We Can
St = {}

p1 = 1e5 #Pa
x1 = 1 #quality
St[1] = stater('P',p1,'Q',x1,'water')

p2 = p1  #pressure doesn't drop through ideal HE
T2 = 20 + 273 #K
St[2] = stater('P',p2,'T',T2,'water')
print state_table(St)
T3 = 275. #K
p3 = 1e5 #Pa

T4 = 290. #K
p4 = p3 #Pa

#Set mass flow rate ratios
m_air = 170
m_water = 1.

#given
cp_air = 1.005 #kJ/(kg K)

#System Model
#Qdot is _not_ Zero
#Wdot = 0
# 0  = Qdotcv + mair h3 + mwater h1 - mair h4 - mwater h2

Qdotcv_waternormalized = (m_air/m_water)*cp_air*(T4-T3) + (St[2]['H']-St[1]['H'])/1000 # kJ/kg (of water)

print "The heat lost to the atmosphere through the boundary is %.2f kJ/(kg water)" % Qdotcv_waternormalized


#Now calculate the entropy generated at a distance where T = 275 K

# 0 = Qcv/Tb + mair(s3-s4) + mwater(s1-s2) + s_gen
# sgen = -s_in - s_water - s_air 
s_in = Qdotcv_waternormalized/T3
s_water = (St[1]['S']-St[2]['S']) / 1000
s_air = (m_air/m_water)*cp_air*log(T3/T4)

sgen = -s_in - s_water - s_air

print "The entropy generated is %.2f kJ/(kg water)" % sgen

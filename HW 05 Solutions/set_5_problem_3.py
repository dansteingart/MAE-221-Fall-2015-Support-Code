from pithy import *

"""Air is confined to one side of a rigid container divided by a partition. The other side is initially evacuated. The air is initially at p1=5bar, T1=500K, and V1=0.2m3. When the partition is removed, the air expands to fill the entire chamber. Measurements show that V2=2V1 and p2=p1/4. Assuming the air behaves as an ideal gas, determine (a) the final temperature, in K, and (b) the heat transfer, kJ.
"""

p1 = 5e5 #Pa
T1 = 500. #k
V1 = 0.2 #m^3
R = 8314.4 #kJ/(mol K)
m_air = 28.97 #K
R_air = R/m_air

M = p1*V1/(R_air*T1)

V2 = V1/2
p2 = p1/4.

#PV = RT
T2 = T1*(V1/V2)*(p2/p1)
print "The Final T is", T2, "K"

W12 = 0
U1 = stater('P',p1,'T',T1,'air')['U']
U2 = stater('P',p2,'T',T2,'air')['U']
Q12 = W12 + M*(U2-U1) 
print "The heat transfer is ",Q12/1000,"kJ"
print ""
print "Everything!"
whos(locals())

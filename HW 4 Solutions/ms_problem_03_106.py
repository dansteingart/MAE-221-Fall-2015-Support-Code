from pithy import *

T1 = 27+273 #K
P1 = (101.32+300) * 1000 #Pa, absolute
P2 = (101.32+367) * 1000 #Pa, absolute

#P1 V1 = nR T1; P2 V1 = nR T2
#V1/nR = P1/T1 = P2/T2
T2 = (P2/P1)*T1

whos(locals())
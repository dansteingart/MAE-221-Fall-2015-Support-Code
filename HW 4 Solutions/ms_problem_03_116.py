from pithy import *

m = 2 #kg
R = 8.31446
M = 32
k = 1.35

#State 1
V1 = 2 #m^3
P1 = 1*100#Pa

#State 2
P2 = P1
V2 = 2*V1

#Use IDL to find T1 and T2
T1 = P1*V1/(m*(R/M)) 
T2 = (V2/V1)*T1

#Find c_v
c_v = (R/M)/(k-1)

#Now solve for Q using first law
W  = P1*(V2-V1)
dU = 2*c_v*(T2-T1)
Q = dU + W 

whos(locals())

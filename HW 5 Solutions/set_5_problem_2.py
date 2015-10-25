from pithy import *

"""A piston cylinder assembly contains air modeled as an ideal gas with a constant specific heat ratio, k = 1.4. The air undergoes a power cycle consisting of four processes in series:

Process 1-2: Constant temperature expansion at 600 K from p1=5.5MPa to p2=0.4MPa

Process 2-3: Polytropic expansion with n=k to p3=0.3MPa
Process 3-4: Constant-pressure compression to V4=V1
Process 4-1: Constant-volume heating

Sketch the cycle on a py diagram. Determine (a) the work and heat transfer for each process, in kJ/kg, and (d) the thermal efficiency for the entire process (W/Q)

http://steingart.princeton.edu:8004/mae221fall2015/problem_set_05#4
"""


k = 1.4 #Heat Ratio
m_air = 28.97 #g/mol
R = 8.31446
R_air = R/m_air
cv_air = R_air/(k-1)

#State 1
T1 = 600 #K
p1 = 5e5 #Pa
#pv = R_air T
v1 = R_air*T1/p1

#State 2 
T2 = 600 #K, Constant Temperature Explantion
p2 = 4e5 #Pa
#p1v1 = p2v2
v2 = p1*v1/p2


#State 3, polytropic expansion pv**n = c
p3 = 3e5 #Pa
#p3v3^k = p2v2^k
v3 =  (p2*v2**k/p3)**(1/k)
#pv = R_Air T
T3 = p3*v3/R_air

#State 4, Constant-pressure compression to V4=V1
p4 = p3
v4 = v1 
#v4/v3 = T3/T4
T4 = T3*v4/v3

P = [p1,p2,p3,p4,p1]
V = [v1,v2,v3,v4,v1]

vs12 = linspace(v1,v2,100)
ps12 = (p1*v1**1)/vs12**1

vs23 = linspace(v2,v3,100)
ps23 = (p2*v2**k)/vs23**k

vs34 = linspace(v3,v4,100)
ps34 = linspace(p3,p4,100)

vs41 = linspace(v4,v1,100)
ps41 = linspace(p4,p1,100)


print ps12
plot(V,P,'k.',markersize=10)
for i in range(4): annotate(" State "+str(i+1),xy=(V[i],P[i]))
plot(vs12,ps12,'r')
plot(vs23,ps23,'r')
plot(vs34,ps34,'r')
plot(vs41,ps41,'r')
ylim(2e5,5.5e5)
xlim(3e-4,5.8e-4)
ylabel("Pressure (Pa)")
xlabel("Volume (m^3/kg)")
showme()
clf()


#Process 1-2
U12 = cv_air*(T2-T1)
W12 = R_air * T1 * log(v2/v1)
Q12 = U12 + W12

#Process 2-3
W23 = (p3*v3-p2*v2)/(1-k)
U23 = cv_air*(T3-T2)
Q23 = round(U23 + W23,2) 

#Process 3-4
W34 = p3*(v4-v3)
U34 = cv_air*(T4-T3)
Q34 = round(U34 + W34,2) 

#Process 3-4
W41 = (v4-v1)
U41 = cv_air*(T1-T4)
Q41 = round(U41 + W41,2) 

Qin = Q12 + Q41
Wcycle = W12+W23+W34+W41
eta = Wcycle/Qin
whos(locals())







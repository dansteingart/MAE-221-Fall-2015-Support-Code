from pithy import *

St ={}

#Problem Statement:
#http://steingart.princeton.edu:8004/mae221fall2015/problem_set_08#2
#Set the States:

T1 = 28+273 #K
p1 = 12e5
St[1] = stater('T',T1,'P',p1,'R22')

T2 = 20+273 #K
p2 = p1
St[2] = stater('T',T2,'P',p1,'R22')

p3 = 2e5
x3 = 1
St[3] = stater('Q',x3,'P',p3,'R22')

#m1 = m2
#Solve for state 4 using the first law
#Qcvdot = 0
#KE = 0
#PE = 0

#m*h1 + m*h3 - m*h2-m*h4 = 0

h4 = St[1]['H']+St[3]['H']-St[2]['H']
p4 = p3
St[4] = stater('H',h4,'P',p4,'R22')

print state_table(St)

#now calculate entropy generated

#0 = s1-s2 + s3-s4 + sgen

sgen = St[2]['S']+St[4]['S']-St[1]['S']-St[3]['S']

print "The entropy generated is %.3f kJ/(K kg)" % (sgen/1000)


print "The entropy generated is due to irreversible heat transfer between streams"


#Extra !

ts_phase_envelope('R22')
ss1 = [St[1]['S'],St[2]['S']]
Ts1 = [St[1]['T'],St[2]['T']]
ss2 = [St[3]['S'],St[4]['S']]
Ts2 = [St[3]['T'],St[4]['T']]
print Ts1
plot(ss1,Ts1,'red',linewidth=3)
plot(ss2,Ts2,'green',linewidth=3)
ylabel("Temperature (K)")
xlabel("Entropy (J/(kg K))")
showme()
clf()


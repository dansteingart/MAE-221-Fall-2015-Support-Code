from pithy import *

#6.84
#An inventor claims that at steady state the device shown in Fig. P6.84 develops power from entering and exiting streams of water at a rate of 1174.9 kW. The accompanying table provides data for inlet 1 and exits 3 and 4. The pressure at inlet 2 is 1 bar. Stray heat transfer and kinetic and potential energy effects are negligible. Evaluate the inventor's claim.

print "<center><img style='width:500px' src='http://steingart.princeton.edu:8002/static/realfiles/mae221fall2015/ss_1447619454.png'></center>"

St = {}

m1 = 4. #kg/s
p1 = 1e5 #Pa
T1 = 450+273 #K
St[1] = stater('P',p1,'T',T1,'water')


m3 = 5. #kg/s
p3 = 2e5 #Pa
T3 = 200+273 #K
St[3] = stater('P',p3,'T',T3,'water')

m4 = 3. #kg/s
p4 = 4e5 #Pa
T4 = 400+273 #K
St[4] = stater('P',p4,'T',T4,'water')

W = 1174.9*1000 #J

#Solve for state 2
#m1 + m2 = m3 + m4
p2 = 1e5
m2 = m3 + m4 - m1 
h2 = (W - m1*St[1]['H']+ m3*St[3]['H'] + m4*St[4]['H'])/m2
St[2] = stater('P',p2,'H',h2,'water')

print "h2 = %.2f kJ/kg" % (h2/1000)

#now solve for S
#0 = Q/Tb + m1*s1 + m2*s2 - m3*s3 - m4*s4 + s_gen
Q = 0
Tb = 300 #doesn't matter b/c Q = 0
s_gen = Q/Tb - m2*St[2]['S'] - m1*St[1]['S'] + m3*St[3]['S'] + m4*St[4]['S']

print "The generated entropy is %.2f kJ/(K kg) " % (s_gen/1000)
print "The process is impossible"
print state_table(St)

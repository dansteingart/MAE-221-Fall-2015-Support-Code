from pithy import *

St = {}
#States
p1 = 40e5
T1 = 500+273
AV1 = 90/60. #m^3/s
St[1] = stater('P',p1,'T',T1,'water')

p2 = 20e5
T2 = 400+273
St[2] = stater('P',p2,'T',T2,'water')

p3 = p2
T3 = T1
St[3] = stater('P',p3,'T',T3,'water')

x4 = 1
p4 = 0.6e5
St[4] = stater('P',p4,'Q',x4,'water')

#a) Determine mdot
mdot = AV1*St[1]['D']
print "The mass flow rate is %.2f kg/s" % mdot#

#b) Determine W_dots
W_dot_12 = - mdot*(St[2]['H']-St[1]['H']) 
W_dot_34 = - mdot*(St[4]['H']-St[3]['H']) 
print "W_dot_12 is %.2f kW" % (W_dot_12/1000)#
print "W_dot_34 is %.2f kW" % (W_dot_34/1000)#

#c) Determine Q_dot_in
Q_dot_in = mdot*(St[3]['H']-St[2]['H']) 
print "Q_dot_in is %.2f kW" % (Q_dot_in/1000)#


#Beyond scope of question, but helpful for understanding what is happeningc6
print state_table(St)

pv_phase_envelope('water')
Vs = []
Ps = []
for i in range(1,5): 
    Vs.append(St[i]['V'])
    Ps.append(St[i]['P'])
    annotate("(%i)" % i, xy=(St[i]['V'],St[i]['P']),fontsize=9)
plot(Vs,Ps,'r.-')
loglog()
xlim(5e-3,1e1)
xlabel("Volume (m^3/kg)")
ylabel("Presure (Pa)")
showme()
clf()
from pithy import *

#6.79 Air enters a turbine operating at steady state at 8 bar, 1400 K and expands to 0.8 bar. The turbine is well insulated, and kinetic and potential energy effects can be neglected. Assuming ideal gas behavior for the air, what is the maximum theoretical work that could be developed by the turbine in kJ per kg of air flow?

St = {}

p1 = 8e5 #Pa
T1 = 1400 #K
St[1] = stater('P',p1,'T',T1,'air')

p2 = 8e4 #Pa
s2 = St[1]['S']
St[2] = stater('P',p2,'S',s2,'air')

Wbym = (St[1]['H'] - St[2]['H'])/1000


print state_table(St)

print "The maximum work available from the systems is %.2f kJ/kg" % Wbym

vs = [St[1]['V'],St[2]['V']]
Ps = [St[1]['P'],St[2]['P']]
ss = [St[1]['S'],St[2]['S']]
Ts = [St[1]['T'],St[2]['T']]

plot(vs,Ps)
ylabel("Pressure (Pa)")
xlabel("Volume (m^3/kg)")
showme()
clf()

plot(ss,Ts)
xlabel("s (J/(kg*K))")
ylabel("T (K)")
showme()
clf()
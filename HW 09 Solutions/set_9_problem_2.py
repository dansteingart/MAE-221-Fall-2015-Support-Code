from pithy import *

St = {}

p1 = 20e6 #Pa
T1 = 560 + 273
St[1] = stater('P',p1,'T',T1,'water')

#Solve for the real state using the isentrooic efficiency.
p2 = .5e5 #Pa
St['2s'] = stater('P',p2,'S',St[1]['S'],'water')
eta_turbine = .81
h2 = St[1]['H'] - (St[1]['H']-St['2s']['H'])*eta_turbine
St[2] = stater('P',p2,'H',h2,'water')

p3 = .4e5 #Pa
T3 = 273+75 #K
St[3] = stater('P',p3,'T',T3,'water')

#Solve for the real state using the isentrooic efficiency.  Note!  We _divice_ by the isentropic efficiency here since the enthalpy needed to pressurize the fluid _increases_ 
p4 = p1 #Pa
eta_pump = .85
St['4s'] = stater('P',p4,'S',St[3]['S'],'water')
h4 = St[3]['H'] - (St[3]['H']-St['4s']['H'])/eta_pump
St[4] = stater('P',p4,'H',h4,'water')

p5 = 1e5 #Pa
T5 = 273+20 #K
St[5] = stater('P',p5,'T',T5,'water')
 
p6 = 1e5 #Pa
T6 = 273+38 #K
St[6] = stater('P',p6,'T',T6,'water')

m_dot_cooling = 70.7 #kg/s

print state_table(St)

print "Using a first law balance across the condensing heat exchanger"

m_dot_steam = m_dot_cooling*(St[6]['H']-St[5]['H'])/(St[2]['H']-St[3]['H'])

print "The mass flow rate of steam is %.2f kg/s" % m_dot_steam

print ""
print "Solve for the thermal efficieny"


W_net = m_dot_steam*((St[1]['H']-St[2]['H'])+(St[3]['H']-St[4]['H']))
Q_in  = m_dot_steam*((St[1]['H']-St[4]['H']))
eta = 100*W_net/Q_in
print "The thermal effiency is "+"%.2f" % eta +"%"

from pithy import *

p = [18,7,7,18]
h = [276.83,261.01,86.78,87.93] #kJ/kg
x = [1,.9952,0]
R_in = .3*.6 # kW/m^2

W_dot_cycle = 1 # kW


W_turbine = h[0]-h[1] #kJ/kg
W_pump = h[2]-h[3]    #kJ/kg
Q_out = h[1]-h[2]     #kJ/kg
Q_in = h[0]-h[3]      #kJ/kg

m_dot = W_dot_cycle/(W_turbine + W_pump) #kg/s per kW produced

print "The mass flow rate per kW net work is %.2f kg/s" % m_dot

Q_dot_in = m_dot * Q_in 
print "The heat in per kW net work is %.2f kW" % Q_dot_in

Q_dot_collector = (Q_dot_in/.6)
print "The heat coming into the collector per kW net work is %.2f kW" % Q_dot_collector

surface_area = Q_dot_collector/.3 
print "The collector surface area per kW produced is %.2f m^2" % surface_area

#make state table: NOTE, we have to reference the coolprops enthalpies, not the stated enthalpies. Also note that the _difference_ is still the same
St = {}
for i in range(3): St[i+1] = stater('P',p[i]*1e5,'Q',x[i],"R134a")
St[4] = stater('P',p[3]*1e5,'H',St[3]['H']-W_pump*1000,'R134a')

print state_table(St)
print """There are two areas of improvement: 
1) There is significant heat loss between the collector and the fluid.  Better contact here will reduce the surface area per kW net
2) The turbine is not isentropic, though it is as close as we are going to get.
"""



from pithy import *

p = [12e6,1e6,6e3,6e3,12e6,12e6,1e6,6e3] #Pa
h = [3506.2,2823.3,2058.2,151.53,163.60,606.61,762.81,762.81]
h = array(h)*1e3 # J/kg

St = {}

for i in range(8):
    St[i+1] = stater('P',p[i],'H',h[i],'water')
    
print state_table(St)


print "First find the mass flow fraction split into the regen cycle"

y = (St[6]['H']-St[5]['H'])/(St[2]['H']-St[7]['H'])

print "mdot1 = mdot2 + mdot3 = y*mdot1 + (1-y)*mdot1"
print "Balance across the closed feedwater heater"
print "y*m1dot*(h2-h7) = mdot1*(h6-h5)"
print "y = %.3f" %y
print 


W_turbine = (St[1]['H']-St[2]['H'])+(1-y)*(St[2]['H']-St[3]['H'])
W_pump = (St[4]['H']-St[5]['H'])
Q_in =   (St[1]['H']-St[6]['H'])

eta = (W_turbine+W_pump)/(Q_in)

print "now, based on m1, find the work through the split turbine"
print "W_turbine = (h1-h2)+(1-y)(h2-h3= %.2f kJ/kg" % (W_turbine/1000)
print "and the pump"
print "W_pump = h4 - h5 = %.2f kJ/kg" % (W_pump/1000)
print "finally the boiler"
print "Q_in = h1-h6 = %.2f kJ/kg" % (Q_in/1000)
print "now the thermal efficiency"
print "eta = (W_turbine+W_pump)/(Q_in) =%.2f" % eta
print

print "now caculate the mass flow rate"
W_dot_net = 330e6 #W
m_dot = W_dot_net/(W_turbine+W_pump)
print "m_dot = W_dot_net/(W_turbine+W_pump) = %.1f kg/s" % m_dot 
print

print "now calculate the rate of entropy production in the feedwater heater, assuming adiabatic operation"
sigma_ofh = m_dot*(St[6]['S']-St[5]['S'])+y*m_dot*(St[7]['S']-St[2]['S'])
print "sigma_ofh = m_dot*(s6-s5)+y*m_dot*(s7-s2) = %.2f kW/K" %(sigma_ofh/1000)
print

print "now calculate the rate of entropy production in the steam trap, assuming adiabatic operation"
sigma_st = m_dot*y*(St[8]['S']-St[7]['S'])
print "sigma_ofh = m_dot*y*(s8-s7) = %.2f kW/K" %(sigma_st/1000)

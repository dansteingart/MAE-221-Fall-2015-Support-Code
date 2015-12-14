from pithy import *

p = [1.5e6,0.2e6,0.1e5,0.1e5,1.5e6,1e5,.1e5] # Pa
h = [2992.7,2652.9,2280.4,191.83,193.34,251.13,251.13]
h = array(h)*1000 #kJ/kg

St = {}

for i in range(7):
    St[i+1] = stater('P',p[i],'H',h[i],'water')
    
print state_table(St)

mdot1 = 1 #kg/s

y = .15 #Flow extracted to co-gen

print "a) Find the heat transfer to the boiler"
Q_dot_in = mdot1*(St[1]['H']-St[5]['H'])
print "Q_dot_in = mdot1*(h1-h5) = %.2f kW" % (Q_dot_in/1000)
print

print "b) Find the net power delivered"
W_dot_t = mdot1*(St[1]['H']-St[2]['H'])+(1-y)*mdot1*(St[2]['H']-St[3]['H'])
print "W_dot_t = mdot1*(h1-h2)+mdot1*(1-y)*(h2-h3) = %.2f kW" % (W_dot_t/1000)
W_dot_p = mdot1*(St[4]['H']-St[5]['H'])
print "W_dot_p = mdot1*(h4-h5) = %.2f kW" % (W_dot_p/1000)
W_dot_net = W_dot_t+W_dot_p
print "W_dot_net = W_dot_t+W_dot_p = %.2f kW" % (W_dot_net/1000)
print

print "c) Find the heat to the heating load"
Q_dot_load = y*mdot1*(St[6]['H']-St[2]['H'])
print "Q_dot_load = y*mdot1*(h6-h2) = %.2f kW" % (Q_dot_load/1000)
print

print "d) Find the heat to the condenser"
Q_dot_cond = -y*mdot1*(St[7]['H'])-(1-y)*mdot1*(St[3]['H'])+mdot1*(St[4]['H'])
print "Q_dot_cond = -mdot1*(y*h7+(1-y)*h3-h4) = %.2f kW" % (Q_dot_cond/1000)
print

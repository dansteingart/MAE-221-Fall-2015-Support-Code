from pithy import *

# Water is the working fluid in a Rankine cycle with reheat. Superheated vapor enters the turbine at 10 MPa, 480 C, and the condenser pressure is 6 kPa. Steam expands through the first-stage turbine to 0.7 MPa and then is reheated to 480 C. Determine for the cycle
# (a) the heat addition, in kJ per kg of steam entering the first-stage turbine.
# (b) the thermal efficiency.
# (c) the heat transfer from the working fluid passing through the condenser to the cooling water, in kJ per kg of steam entering the first-stage turbine.

# (d) The mass flow rates of the water within the rankine cycle and of the cooling water if the output temperature of the cooling stream is limited to only 5 C warmer than the input and the net power must be 10 MW. 

# Assume the pump and each turbine stage have an isentropic efficiency of 80%, and that the condenser in a closed two stream heat exchanger which is cooled from a local river with an inlet temperature of 15 C

eta_tool = 0.8 #for all comps and turbs

St = {}

T1 = 600+273
P1 = 20e6
St[1] = stater('T',T1,'P',P1,'water')

#Through First Turbine
P2 = 0.7e6 #Pa
s2s = St[1]['S']
St['2s'] = stater('S',s2s,'P',P2,'water')
h2 = St[1]['H']-eta_tool*(St[1]['H']-St['2s']['H'])
St[2] = stater('H',h2,'P',P2,'water')

#Reheat to T1
P3 = P2
T3 = T1
St[3] = stater('T',T3,'P',P3,'water')

#Through Second Turbine
P4 = 6e3 #Pa
s4s = St[3]['S']
St['4s'] = stater('S',s4s,'P',P4,'water')
h4 = St[3]['H']-eta_tool*(St[3]['H']-St['4s']['H'])
St[4] = stater('H',h4,'P',P4,'water')

#Through The Condenser
x5 = 0
P5 = P4
St[5] = stater('Q',x5,'P',P5,'water')

#The the Pump
P6 = P1 #Pa
s6s = St[5]['S']
St['6s'] = stater('S',s6s,'P',P6,'water')
h6 = St[5]['H']-(St[5]['H']-St['6s']['H'])/eta_tool
St[6] = stater('H',h6,'P',P6,'water')

#Inlet cooling stream
T7 = 273+15 #K
P7 = 1e5 #Pa
St[7] = stater('T',T7,'P',P7,'water')

#Outlet cooling stream (max)
T8 = T7+5 #K
P8 = P7 #Pa
St[8] = stater('T',T8,'P',P8,'water')

print state_table(St)

print "(part a) the heat addition, in kJ per kg of steam entering the first-stage turbine."

Q_in_1   =  (St[1]['H']-St[6]['H'])/1000 #kJ/kg
Q_in_2   =  (St[3]['H']-St[2]['H'])/1000 #kJ/kg
W_turb_1 =  (St[1]['H']-St[2]['H'])/1000 #kJ/kg
W_turb_2 =  (St[3]['H']-St[4]['H'])/1000 #kJ/kg
W_pump   =  (St[1]['H']-St[6]['H'])/1000 #kJ/kg
Q_out    =  (St[5]['H']-St[4]['H'])/1000 #kJ/kg
eta = 1 - (-Q_out/(Q_in_1+Q_in_2))
W_net = W_turb_1 + W_turb_2 + W_pump

print "Q_in_1 = h1-h6 = %.2f kJ/kg" % Q_in_1
print
print "(part b) the thermal efficiency of the cycle"
print "eta = 1 - (-Q_out/(Q_in_1+Q_in_2)) = %.2f" % eta
print
print "(part c) the heat transfer from the working fluid passing through the condenser to the cooling water, in kJ per kg of steam entering the first-stage turbine."
print "Q_out  = h5-h4 = %.2f kJ/kg" % Q_out
print

print "(part d) The mass flow rates of the water within the rankine cycle and of the cooling water if the output temperature of the cooling stream is limited to only 5 C warmer than the input and the net power must be 10 MW. "
W_dot_req = 10000 # KW
m_dot_cycle = W_dot_req/W_net #kg/s
m_dot_cooling = m_dot_cycle*(St[5]['H']-St[4]['H'])/(St[7]['H']-St[8]['H'])
print "m_dot_cycle = W_dot_req/W_net = %.2f kg/s" % m_dot_cycle
print "m_dot_cooling = m_dot_cycle*Q_out/(h8-h7) = %.2f kg/s" % m_dot_cooling





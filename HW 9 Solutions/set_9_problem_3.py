from pithy import *

p = [160,15,15,1.5,15,160]
p = array(p)*1e5 #Pa
h = [3353.3,2792.2,3169.2,2693.6,467.11,486.74]
h = array(h)*1000  #J/kg
hdiff = array(h)-h[1]

St = {}
ref = stater('P',p[1],'Q',1,'water')

for i in range(6):
    St[i+1] = stater('P',p[i],'H',hdiff[i]+ref['H'],'water')

print state_table(St)

print "To determine the mass fraction through reheat, solve for the heat find both Q_in's and W_turbines"

m_dot = 2.3 #kg/s

Q_dot_in_1 = m_dot*(St[1]['H']-St[6]['H'])
Q_dot_in_2 = m_dot*(St[3]['H']-St[2]['H'])
W_dot_tb_1 = m_dot*(St[1]['H']-St[2]['H'])
W_dot_tb_2 = m_dot*(St[3]['H']-St[4]['H'])
W_dot_pump = m_dot*(St[5]['H']-St[6]['H'])

W_dot_cycle = W_dot_tb_1 + W_dot_tb_2 + W_dot_pump
Q_dot_total = Q_dot_in_1 + Q_dot_in_2

print "The Total Work is %.2f kW" % (W_dot_cycle/1000) 
print "The Total Heat in is %.2f kW" % (Q_dot_total/1000) 
print "The Thermal Efficiency is %.2f" % (W_dot_cycle/Q_dot_total)
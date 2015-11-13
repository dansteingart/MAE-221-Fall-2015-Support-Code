from pithy import *

St = {}

#Define States
T1 = 300 #K
P1 = 1e5 #Pa
St[1] = stater('P',P1,'T',T1,'air')
m_dot_air = 0.6 #kg/s

T2 = 600 #K
P2 = 3e5 #Pa
St[2] = stater('P',P2,'T',T2,'air')

T3 = 450 #K
P3 = P2 #Pa
St[3] = stater('P',P3,'T',T3,'air')

T4 = 800 #K
P4 = 9e5 #Pa
St[4] = stater('P',P4,'T',T4,'air')

T5 = 20 + 273 #K
P5 = 1e5 #Pa
St[5] = stater('P',P5,'T',T5,'water')

T6 = 30 + 273 #K
P6 = P5 #Pa
St[6] = stater('P',P6,'T',T6,'water')

#Power Required for Compressors
W_dot_A = - m_dot_air * (St[2]['H']-St[1]['H'])
W_dot_B = - m_dot_air * (St[4]['H']-St[3]['H'])
W_dot_total = W_dot_A+W_dot_B

print "The total Power Required is %.2f kw" % (W_dot_total/1000)

#Mass flow rate of water

#m_dot_water * (h6-h5) = m_dot_air*(h3-h2)

m_dot_water = m_dot_air*(St[3]['H']-St[1]['H'])/(St[6]['H']-St[5]['H'])

print "The mass flow rate of water is %.2f kg/s" % (m_dot_water)





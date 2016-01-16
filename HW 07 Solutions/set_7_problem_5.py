from pithy import *

#Problem 6.110
#Figure P6.110 shows an air compressor and regenerative heat exchanger in a gas turbine system operating at steady state. Air flows from the compressor through the regenerator, and a separate stream of air passes though the regenerator in counterflow. Operating data are provided on the figure. Stray heat transfer to the surroundings and kinetic and potential energy effects can be neglected. The compressor power input is 6700 kW. Determine the mass flow rate of air entering the compressor, in kg/s, the temperature of the air exiting the regenerator at state 5, in K, and the rates of entropy production in the compressor and regenerator, in kW/K.

print "<center><img style='width:500px' src='http://steingart.princeton.edu:8002/static/realfiles/mae221fall2015/ss_1447619994.png'></center>"

#Build out states


St = {}

T1 = 300 #K
p1 = 1e5 #Pa
St[1] = stater('P',p1,'T',T1,'air')

T2 = 620 #K
p2 = 12e5 #Pa
St[2] = stater('P',p2,'T',T2,'air')

T3 = 760 #K
p3 = 12e5 #Pa
St[3] = stater('P',p3,'T',T3,'air')

T4 = 780 #K
p4 = 1e5 #Pa
St[4] = stater('P',p4,'T',T4,'air')

p5 = 1e5 #bar
#Solve for T5
#m1(h2-h3) = m4(h4-h5) ==> m1 = m4 so
h5 = St[2]['H'] - St[3]['H'] + St[4]['H']
St[5] = stater('P',p5,'H',h5,'air')

#For comparison's sake:
T5 = T2-T3+T4
print "Assuming constant cp, T5 =", T5,"K, accounting for pressure change (12 Bar to 1 Bar), T5 =", round(St[5]['T'],3),"K.  Note that the enthalpy is a much stronger function of temperature than pressure."

print state_table(St)

#Calculate m_dot
W = -6700e3 # J/kg
m_dot = W/(St[1]['H'] - St[2]['H'])
print "The mass flow rate is %.2f kg/s" % m_dot

print ""
#Calculate entropy generated by the compressor
Qcv_comp = 0
R = 8.31446/28.97

sigma_comp = m_dot*((St[2]['S'] - St[1]['S']))/1000
print "The entropy production at the compressor is %.2f kW/K" % sigma_comp

#If you are using table A22 you need to account for the change in pressure separately.  
#sigma_comp = m_dot*((St[2]['S'] - St[1]['S']) - R*log(p2/p1))/1000


#Calculate entropy generated by the heat exchanger
Qcv_comp = 0
sigma_heat = m_dot*(St[3]['S'] - St[2]['S'] + St[5]['S']-St[4]['S'])/1000
print "The entropy production at the heat exchanger is %.2f kW/K" % sigma_heat


from pithy import *
from CoolProp.CoolProp import Props
#what do we know
T_1 = 273+21.1 #in K
p_1 = 1*100 #1 bar in kPa
p_2 = 5*100 #1 bar in kPa
R = 8.31415 #kJ/kmol-K
m_air = 28.97 #kg/kmol


print "Part a) Find W/m and Q/m if n = 1.3"
n = 1.3
#Find T_2
T_2 = T_1*(p_2/p_1)**((n-1)/n)
print "T_2 = ",round(T_2,2),"K" 

#Find W_M
W_m = R/m_air * (T_2 - T_1)/(1-n)
print "W_m = ",round(W_m,2),"kJ/kg" 

#Find Q/m
#look up c_v, assume constant for this range
c_v = Props('O','T',T_1,'P',p_1,'air') #O is c_v 
# http://www.coolprop.org/apidoc/CoolProp.html#CoolProp.CoolProp.Props

Q_m = W_m + c_v*(T_2-T_1)
print "Q_m = ",round(Q_m,2),"kJ/kg" 
c_v 
print ""
print "Part b) Find W/m and Q/m if n = k"
#find k
k = 1+(R/m_air)/c_v
n = k
T_2 = T_1*(p_2/p_1)**((n-1)/n)
print "T_2 = ",round(T_2,2),"K" 

#Find W_M
W_m = R/m_air * (T_2 - T_1)/(1-n)
print "W_m = ",round(W_m,2),"kJ/kg" 

#Find Q/m
Q_m = W_m + c_v*(T_2-T_1)
print "Q_m = ",round(Q_m,2),"kJ/kg" 

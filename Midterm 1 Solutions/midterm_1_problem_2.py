from pithy import *


mc = 13 #kg
Tc = 27+273 #k
cc = 0.385 #kJ/kg K

mw = 4 #kg
Tw = 50+273 #k
cw = 4.18#kJ/kg K

W_res = -100 #kJ

#mc cc (Tf-Tc) + mw cw (Tf- Tw) = -W_res

Tf = (mc*cc*Tc + mw*cw*Tw - W_res)/(mc*cc+mw*cw)

print "The final temperature is",round(Tf-273,2),"C"


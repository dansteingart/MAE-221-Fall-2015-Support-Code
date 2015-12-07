from pithy import *

p1 = 1e5 * 100 #Pa
p2 = .1 * 1e5 #Pa
T1 = 600 + 273
x2 = .92

V = 0.36 # m^3/s

#Look up states
St = {}
St[1] = stater('P',p1,'T',T1,'water')
St[2] = stater('P',p2,'Q',x2,'water')
St['2s'] = stater('P',p2,'S',St[1]['S'],'water')

print state_table(St)

print "<h3>A) Calculate the Mass Flow Rate</h3>"

mdot = V*St[1]['D']
print "mdot = V*St[1]['V'] = ", round(mdot,2), "kg/s"

print "<h3>B) Calculate the Power Developed</h3>"

Wcv_dot = mdot*(St[1]['H']-St[2]['H'])/1000
print "Wcv_dot = mdot*(St[1]['H']-St[2]['H'])/1000 =", round(Wcv_dot,2), "kW"

print "<h3>C) Calculate the Rate of Entropy Production</h3>"
sigmacv_dot = mdot*(St[2]['S']-St[1]['S'])/1000
print "sigmacv_dot = mdot*(St[2]['S']-St[1]['S']) =", round(sigmacv_dot,2), "kW/K"


print "<h3>D) Calculate the Turbine Efficiency</h3>"

eta_s = (St[1]['H']-St[2]['H'])/(St[1]['H']-St['2s']['H'])

print "eta_s = (St[1]['H']-St[2]['H'])/(St[1]['H']-St[2s]['H'])=", round(eta_s,2)

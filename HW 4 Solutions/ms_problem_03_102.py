from pithy import *

R_E = 1545 
print "Part A: Water Vapor" 

P = 4000 * 144 #psi to psf
V_table = 0.1752 #ft^3/lb
T = 1000+460 #Rankine
M = 18.02
V_idg = (R_E/M)*T/P
error = str(100*abs(V_idg-V_table)/V_table)[0:4]+"%"
whos(locals())
print
print "Part B: Water Vapor" 
P = 5 * 144 #psi to psf
V_table = 84 #ft^3/lb
T = 250+460 #Rankine
M = 18.02
V_idg = (R_E/M)*T/P
error = str(100*abs(V_idg-V_table)/V_table)[0:4]+"%"
whos(locals())
print
print "Part C: Ammonia" 
P = 40 * 144 #psi to psf
V_table = 7.913 #ft^3/lb
T = 60+460 #Rankine
M = 17.03
V_idg = (R_E/M)*T/P
error = str(100*abs(V_idg-V_table)/V_table)[0:4]+"%"
whos(locals())
print
print "Part D: Air" 
P = 300. * 144 #psi to psf
V_table = 14.108 #ft^3/lb
T = 560 #Rankine
M = 1.42
V_idg = (R_E/M)*T/P
error = str(100*abs(V_idg-V_table)/V_table)[0:4]+"%"
whos(locals())

print
print "Part E: Refrigerant 134" 
P = 300 * 144 #psi to psf
V_table = 0.16333 #ft^3/lb
T = 180+460 #Rankine
M = 102.03
V_idg = (R_E/M)*T/P
error = str(100*abs(V_idg-V_table)/V_table)[0:4]+"%"
whos(locals())



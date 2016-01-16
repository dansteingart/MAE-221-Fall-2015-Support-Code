from pithy import *


Wcycle = 0.6 #kW
Qin = 3.  #kW

Cop_claimed = Qin/Wcycle

Tc = 270. #K
Th = 293. #l


Cop_max = Tc/(Th-Tc)

whos(locals())
print
print "The inventor's process is <b>",
if Cop_claimed <= Cop_max: print "valid",
else: print "invalid",
print "</b>"
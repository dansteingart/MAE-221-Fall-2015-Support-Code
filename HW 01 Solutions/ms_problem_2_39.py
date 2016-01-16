from pithy import *

"""An electric heater draws a constant current of 6 amp, with an applied voltage of 220 V, for 24 h. Determine the instantaneous electric power provided to the heater, in kW, and the total amount of energy supplied to the heater by electrical work, in kWh. If electric power is valued at $0.08/kWh, determine the cost of operation for one day"""


E = 220 #Volts
I = 6 #Amps
t = 24 #Hr
P = E*I #Watts
WpDay = P*t #Joules Per Day
Cost = 0.08 / 1000 #$/kWh
CpDay = WpDay*Cost

print "The heater consumes %.2e W of power and costs $%.2e /day to operate" %(P,CpDay)

whos(locals())
from pithy import *
"""
An industrial process discharges 5.6e3 m3/min of gaseous combustion products at 204.4 C, 1 bar. A proposed system for utilizing the combustion products combines a heat recovery steam generator with a turbine. At steady state, combustion products exit the steam generator at 126.6 C and 1 bar and a separate stream of water enters at 275.8 kPa, and 38.9 C with a mass flow rate of 124.7 kg/min. At the exit of the turbine, the pressure is 6.9 kPA and the quality is 93%. Heat transfer from the outer surfaces of the steam generator and turbine can be ignored, as can the changes in kinetic and potential energies of the flowing streams. There is no significant pressure drop for the water flowing through the steam generator. The combustion products can be modeled as air as an ideal gas.

(a) Determine the power developed by the turbine, in kJ/min.

(b) Determine the turbine inlet temperature.

(c) Evaluating the power developed at 0.08 USD per kW-hr, determine the value of the power, in USD/year, for 8000 hours of operation annually.
"""



AV_1  = 5.6e3/60# m^3/s
T_1   = 205 + 273 #K
P_1   = 1e5 # Pa
St1   = stater('P',P_1,'T',T_1,'air')
mdot_1 = AV_1/St1['V']

T_2  = 126 + 273 #K
P_2  = 1e5 # Pa
St2  = stater('P',P_2,'T',T_2,'air')
mdot_2 = mdot_1

T_3  = 38.9 + 273 # C
P_3  = 275.3 * 1000 # Pa
St3  = stater('P',P_3,'T',T_3,'water')
P_4  = P_3
mdot_3  = 124.7 /60 # kg/s

P_5  = 6.9*1000   # Pa
x_5  = 0.93
St5  = stater('P',P_5,'Q',x_5,'water')

#A
Wdot_turbine = mdot_1*(St1['H']-St2['H'])+mdot_3*(St3['H']-St5['H'])

print "The Turbine in generating: ", round(Wdot_turbine/1000,2), 'kW'

#B
#Solve for State 4 to find T_4
H_4 = St3['H'] + (mdot_1/mdot_3)*(St1['H']-St2['H'])
St4 = stater('P',P_4,'H',H_4,'water')
print "T4 = ", round(St4['T']-273,2), 'C'

#C 
DpKWhr = 0.08
DpY = (Wdot_turbine/1000 * 24*365) * DpKWhr 
print "The plant is generating: ", round(DpY/1000,2), 'K$/year'


print state_table([St1,St2,St3,St4,St5])
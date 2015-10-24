from pithy import *

"""One kg of water initially is at the critical point. (a) If the water is cooled at constant-specific volume to a pressure of 30 bar, determine the quality at the final state.(b) If the water undergoes a constant-temperature expansion to a pressure of 30 bar, determine the specific volume at the final state, in m3/kg.
"""


St = {}

#Step One Critical Point
T1 = pr('Tcrit','water')
P1 = pr('Pcrit','water')

St[1] = stater('P',P1,'T',T1+.001,'water')

P2 = 3e6
D2 = St[1]['D']
St['2a'] = stater('P',P2,'D',D2,'water')

P2 = 3e6
T2 = St[1]['T']
St['2b'] = stater('P',P2,'T',T2,'water')


print state_table(St)

pv_phase_envelope('water')
for k in St.keys():
    plot(St[k]['V'],St[k]['P'],'k.',markersize=10)
    annotate(" State "+str(k),xy=(St[k]['V'],St[k]['P']))
loglog()
ylabel("Pressure (Pa)")
xlabel("Volume (m^3/kg)")
xlim(1e-4,1e1)

showme()
clf()
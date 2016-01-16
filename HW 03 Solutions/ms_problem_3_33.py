from pithy import *

"""Two kg of Refrigerant 134A undergoes a polytropic process in a piston cylinder assembly from an initial state of saturated vapor at 2 bar to a final state of 12 bar, 80C. Determine the work for
the process, in kJ. """

St = {}
mass = 2
P1 = 2e5
x1 = 1
St[1] = stater('P',P1,'Q',x1,'R134a')

P2 = 12e5
T2 = 80+273
St[2] = stater('P',P2,'T',T2,'R134a')

#Solve for n given p1v1^n = p2v2^n
n = log(St[1]['P']/St[2]['P'])/log(St[2]['V']/St[1]['V'])

Vs = linspace(St[1]['V'],St[2]['V'],100)

def Pd(v,nn): return St[1]['P']*St[1]['V']**n/(v**n)
Ps = Pd(Vs,n)

pv_phase_envelope("R134a")
plot(Vs,Ps,'r')
for k in St.keys():
    plot(St[k]['V'],St[k]['P'],'k.',markersize=10)
    annotate(" State "+str(k),xy=(St[k]['V'],St[k]['P']))
loglog()
ylabel("Pressure (Pa)")
xlabel("Volume (m^3/kg)")
showme()
clf()

work = mass*(St[2]['P']*St[2]['V'] - St[1]['P']*St[1]['V'])/(1-n)
print "The work on tis system is",round(work/1000,2),"J"
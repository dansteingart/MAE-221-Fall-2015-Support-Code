from pithy import *
from CoolProp.CoolProp import PropsSI

"""
MS Example 3.3

A well-insulated rigid tank having a volume of 10 ft^3 contains saturated water vapor at 212F. 
The water is rapidly stirred until the pressure is 20 lbf/in.2

Determine the temperature at the final state, work 
during the process, in Btu.
"""

kPa_to_psi = 1000*101.34/14.7


T1 = 373.15
D1 = PropsSI('D','T',T1,'Q',1,'Water')
D2 = D1 
P1 = 14.7 * kPa_to_psi
P2 = 20 * kPa_to_psi

def ft3tom3(ft3):
    return 0.0283168*ft3

def KtoF(deg):
    return (deg-273)*(9/5.0)+32

def kJkgtoBTUlb(kjkg):
    return kjkg*0.429922614*1e-3 #google

def kgtolb(kg):
    return 2.2 * kg

V1 = ft3tom3(10)
m = kgtolb(D1*V1)

print "m=",m,"lb"

T2 = PropsSI('T','P',P2,'D',D2,'Water')
print "T2=",T2,'K'
print "T2=",KtoF(T2),'F'

u1 = PropsSI('U','T',T1,'P',P1,'Water')
u2 = PropsSI('U','T',T2,'D',D1,'Water')

u1 = kJkgtoBTUlb(u1)
print 'u1=',u1,'btu/lb'
u2 = kJkgtoBTUlb(u2)
print 'u2=',u2,'btu/lb'
print "Delta u =",u2-u1,'kJ/kg'

delU = -(u2-u1)*m
print 'deltaU =',delU,'btu'




##Fancy Stuff to Make Envelope
Psweep = logspace(4,8,1000)
v_sl = 1/PropsSI('D','Q',0,'P',Psweep,'water')
v_sv = 1/PropsSI('D','Q',1,'P',Psweep,'water')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ps = array(list(Psweep)+list(Psweep)[::-1])
plot(vs,Ps,'.2')

plot([1/D1,1/D2],[P1,P2],'ro-')
annotate('State 1',xy=(.2/D1,P1))
annotate('State 2',xy=(.2/D2,P2))

loglog()
xlim([.0001,10])
ylim([1e4,1e6])
xlabel("Specific Volume (m^3/kg)")
ylabel("Pressure (Pa)")
showme()
clf()

Tsweep = linspace(200,600,1000)
v_sl = 1/PropsSI('D','Q',0,'T',Tsweep,'water')
v_sv = 1/PropsSI('D','Q',1,'T',Tsweep,'water')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ts = array(list(Tsweep)+list(Tsweep)[::-1])
plot(vs,Ts,'.2')

plot([1/D1,1/D2],[T1,T2],'ro-')
annotate('State 1',xy=(.2/D1,T1))
annotate('State 2',xy=(.2/D2,T2))

semilogx()
xlim([.0001,10])
#ylim([10,300])
xlabel("Specific Volume (m^3/kg)")
ylabel("Temperature (K)")
showme()
clf()

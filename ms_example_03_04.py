from pithy import *
from CoolProp.CoolProp import PropsSI

'''
MS Example 3.4

Water contained in a piston cylinder assembly undergoes 
two processes in series from an initial state where the 
pressure is 10 bar and the temperature is 400 C. 
Process 1-2: The water is cooled as it is compressed at a 
constant pressure of 10 bar to the saturated vapor state. 
Process 2-3: The water is cooled at constant volume to 150C.

(a) Sketch both processes on Tv and pv diagrams.
(b) For the overall process determine the work.
(c) For the overall process determine the heat transfer.

'''

T1 = 400+273 #C
P1 = 10*100*1e3 #kPa
P2 = P1
T3 = 150+273
q2 = 1
u1 = PropsSI('U','T',T1,'P',P1,'water')
D1 = PropsSI('D','T',T1,'P',P1,'water')
v1 = 1/D1
print 'u1=',u1,'J/kg'
print 'v1=',v1,'kg/m^3'

print "Solve for T2"
T2 = PropsSI('T','P',P1,'Q',q2,'water')
print "T2=",T2-273,"K"

print "Solve for U2"
u2 = PropsSI('U','P',P1,'Q',q2,'water')
print "u2=",u2,"J/kg"

print "Solve for D2,v2"
D2 = PropsSI('D','P',P1,'Q',q2,'water')
v2 = 1/D2
print 'v2=',v2,'kg/m^3'
print "D2=",D2,"kg/m^3"

print "Solve for W/m"
W_m = P1*(v2-v1)
print "W/m=",W_m,"J/kg"

print "Solve for P3"
P3 = PropsSI('P','T',T3,'D',D2,'water')
print "P3=",P3/101.135,"bar"

print "Solve for u3"
u3 = PropsSI('U','T',T3,'D',D2,'water')
print "U3=",u3,"J/kg"

print "Solve for Q/m"
Q_m = (u3-u1) + W_m
print Q_m


v3= v2
whos(locals())


##Fancy Stuff to Make Envelope
Psweep = logspace(4,8,1000)
v_sl = 1/PropsSI('D','Q',0,'P',Psweep,'water')
v_sv = 1/PropsSI('D','Q',1,'P',Psweep,'water')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ps = array(list(Psweep)+list(Psweep)[::-1])
plot(vs,Ps,'.2')

plot([v1,v2,v3],[P1,P2,P3],'ro-')
annotate('State 1',xy=(2*v1,P1))
annotate('State 2',xy=(.2*v2,P2))
annotate('State 3',xy=(.2*v3,P3))

loglog()
xlim([.0001,10])
ylim([1e4,2e6])
xlabel("Specific Volume (m^3/kg)")
ylabel("Pressure (Pa)")
showme()
clf()

Tsweep = linspace(200,700,1000)
v_sl = 1/PropsSI('D','Q',0,'T',Tsweep,'water')
v_sv = 1/PropsSI('D','Q',1,'T',Tsweep,'water')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ts = array(list(Tsweep)+list(Tsweep)[::-1])
plot(vs,Ts,'.2')

plot([v1,v2,v3],[T1,T2,T3],'ro-')
annotate('State 1',xy=(.2*v1,T1))
annotate('State 2',xy=(.2*v2,T2))
annotate('State 3',xy=(.2*v3,T3))

semilogx()
xlim([.0001,10])
#ylim([10,300])
xlabel("Specific Volume (m^3/kg)")
ylabel("Temperature (K)")
showme()
clf()

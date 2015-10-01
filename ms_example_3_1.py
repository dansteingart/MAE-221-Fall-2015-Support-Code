from CoolProp.CoolProp import PropsSI
from pithy import *

"""
MS Example 3.1

A vertical piston cylinder assembly containing 0.1 lb of ammonia, initially a saturated vapor, is placed on a hot 
plate. Due to the weight of the piston and the surrounding atmospheric pressure, the pressure of the ammonia is 20 lbf/in.

Heating occurs slowly, and the ammonia expands at constant pressure until the final temperature is 
77F. Show the initial and final states on T-v and p-v diagrams, and determine

(a) the volume occupied by the ammonia at each end state, in ft
3.

(b) the work for the process, in Btu.

"""
#Givens,converting to SI
m_NH3 = 0.1 * 1/2.2 #lbs to kg
P1 = 20 * 6.894 * 1e3 #psi to Pa
T2 = ((77-32)*(5/9.)) + 273.15 #F to K

#Solve For
#constant pressure process
P2 = P1

#This is a sat vapor at P1, so Quality = 1
T1 = PropsSI('T','Q',1,'P',P1,'ammonia') #K
v1 = 1/PropsSI('D','Q',1,'P',P1,'ammonia') #K
V1 = m_NH3 * v1
v2 = 1/PropsSI('D','T',T2,'P',P2,'ammonia') #K
V2 = m_NH3 * v2

#Calculate work
W = P1*(V2-V1) #J
W_BTU = W*0.94781712*1e-3 #J to BTU

whos(locals())


##Fancy Stuff to Make Envelope
Psweep = logspace(4,8,1000)
v_sl = 1/PropsSI('D','Q',0,'P',Psweep,'ammonia')
v_sv = 1/PropsSI('D','Q',1,'P',Psweep,'ammonia')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ps = array(list(Psweep)+list(Psweep)[::-1])
plot(vs,Ps,'.2')

plot([v1,v2],[P1,P2],'ro-')
annotate('State 1',xy=(.2*v1,P1))
annotate('State 2',xy=(2*v2,P2))

loglog()
xlim([.0001,10])
ylim([1e5,5e5])
xlabel("Specific Volume (m^3/kg)")
ylabel("Pressure (Pa)")
showme()
clf()

##Fancy Stuff to Make Envelope
Tsweep = linspace(200,350,1000)
v_sl = 1/PropsSI('D','Q',0,'T',Tsweep,'ammonia')
v_sv = 1/PropsSI('D','Q',1,'T',Tsweep,'ammonia')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ts = array(list(Tsweep)+list(Tsweep)[::-1])
plot(vs,Ts,'.2')

plot([v1,v2],[T1,T2],'ro-')
annotate('State 1',xy=(.2*v1,T1))
annotate('State 2',xy=(2*v2,T2))

semilogx()
xlim([.0001,10])
#ylim([1e5,5e5])
xlabel("Specific Volume (m^3/kg)")
ylabel("Temperature (K)")
showme()
clf()

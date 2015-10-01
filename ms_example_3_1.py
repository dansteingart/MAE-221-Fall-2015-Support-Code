from CoolProp.CoolProp import PropsSI
from pithy import *

"""
A closed, rigid container of volume 0.5 m3 is placed on a hot plate. Initially, the container holds a two-phase mixture of saturated liquid water and saturated water vapor at p1=1bar with a quality of 0.5. After heating, the pressure in the container is p2=1.5bar. Indicate the initial and final states on a Tv diagram, and determine

(a) the temperature, in C, at states 1 and 2.
(b) the mass of vapor present at states 1 and 2, in kg.
(c) If heating continues, determine the pressure, in bar, when the container holds only saturated vapor.
"""
#Givens
P1 = 1 * 1e5 #Pa
P2 = 1.5 * 1e5 #Pa
V = 0.5 #m^3
Q1 = 0.5 #50/50 liquid to vapor
Q3 = 1 #all vapor


#This is a sat vapor at P1, so Quality = 1
T1 = PropsSI('T','Q',Q1,'P',P1,'water')-273 #K to C
D1 = PropsSI('D','Q',Q1,'P',P1,'water')

#Total mass of the water is constant through the experments
m_total = V*D1

#Calculate the amount of this in liquid and in vapor
m_1_liquid = (1-Q1) * m_total
m_1_vapor  = Q1     * m_total

#Because we're in a closed volume with a fixed mass the specific volume is fixed for anything of Q > 0
D2 = D1
#"Lookup" Q2 and T2, calculate fractions of liquid and vapor in phase 3
Q2 = PropsSI('Q','D',D2,'P',P2,'water')#K to C
T2 = PropsSI('T','Q',Q2,'P',P2,'water')-273 #K to C
m_2_liquid = (1-Q2) * m_total
m_2_vapor  = Q2 * m_total

#At sat vapor per problem statement
D3 = D2

#Cool props can't do 'PropsSI(P,'D',D3,'Q',Q3,'water')', so we improvise

#Make a range of pressures to search
Ps = linspace(1e5,3e5,1000)

#Make a range of densities
Ds = PropsSI('D','P',Ps,'Q',1,'water') 

#Compare Density Range to actual Density and take the closest fit
P3 = Ps[abs(Ds-D3).argmin()]

#Now get the temperature:
T3 = PropsSI('T','Q',Q3,'P',P3,'water')-273 #K to C
whos(locals())


##Fancy Stuff to Make Envelope
Psweep = logspace(4,8,1000)
v_sl = 1/PropsSI('D','Q',0,'P',Psweep,'water')
v_sv = 1/PropsSI('D','Q',1,'P',Psweep,'water')
vs = array(list(v_sl)+list(v_sv)[::-1])
Ps = array(list(Psweep)+list(Psweep)[::-1])
plot(vs,Ps,'.2')

plot([1/D1,1/D2,1/D3],[P1,P2,P3],'ro-')
annotate('State 1',xy=(.2/D1,P1))
annotate('State 2',xy=(.2/D2,P2))
annotate('State 3',xy=(.2/D3,P3))

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
plot(vs,Ts-273,'.2')

plot([1/D1,1/D2,1/D3],[T1,T2,T3],'ro-')
annotate('State 1',xy=(.2/D1,T1))
annotate('State 2',xy=(.2/D2,T2))
annotate('State 3',xy=(.2/D3,T3))

semilogx()
xlim([.0001,10])
ylim([10,200])
xlabel("Specific Volume (m^3/kg)")
ylabel("Temperature (C)")
showme()
clf()

from pithy import *

St = {}

#Write down states
T1 = 160+273 #L
p1 = 5e5 #Pa
St[1] = stater('P',p1,'T',T1,'water')

p2 = 10e5 #Pa
v2 = St[1]['V']
St[2] = stater('P',p2,'D',1/v2,'water')

p3 = p2 #Pa
x3 = 1
St[3] = stater('P',p3,'Q',x3,'water')

v4 = St[3]['V']
T4 = T1
St[4] = stater('T',T4,'D',1/v4,'water')


#Go Through Processes

#1-2 Constant Volume
W12 = 0
U12 = St[2]['U'] - St[1]['U']
Q12 = W12 + U12

#2-3 Constant Presure
W23 = p2*(St[3]['V'] -St[2]['V'])
U23 = St[3]['U'] - St[2]['U']
Q23 = W23 + U23

#3-4 Constant Volume
W34 = 0
U34 = St[4]['U'] - St[3]['U']
Q34 = W34 + U34

#4-1 Isothermal THROUGH PHASE CHANGE
Q41 = 815.8 * 1000
U41 = St[1]['U'] - St[4]['U']
#Q - W = U
W41 = Q41-U41

print state_table(St)


out = "Steps,U(kJ/kg),W(kJ/kg),Q(kJ/kg)\n"
out += "1-2,%.2f,%.2f,%.2f\n" % (U12/1000,W12/1000,Q12/1000)
out += "2-3,%.2f,%.2f,%.2f\n" % (U23/1000,W23/1000,Q23/1000)
out += "3-4,%.2f,%.2f,%.2f\n" % (U34/1000,W34/1000,Q34/1000)
out += "4-1,%.2f,%.2f,%.2f\n" % (U41/1000,W41/1000,Q41/1000)

print csv_to_table(out)

eta = (W12+W23+W34+W41)/(Q12+Q41)

print "The Thermal Efficiency is ", round(eta*100,2),"%"

gamma = (Q23+Q34)/ (W12+W23+W34+W41)

print "The CoP is ", round(gamma,2),""


Ps = []
for i in range(1,5):Ps.append(St[i]['P'])
Vs = []
for i in range(1,5):Vs.append(St[i]['V'])

V41 = linspace(St[4]['V'],St[1]['V'],100)
P41 = stater('T',T1,'D',1/V41,'water')['P']
U41 = stater('T',T1,'D',1/V41,'water')['U']

pv_phase_envelope('water')
plot(Vs,Ps,'k.')
plot(Vs,Ps,'r')
plot(V41,P41,'r')
for i in range(0,4): annotate(str(i+1),xy=(Vs[i],Ps[i]))
xlabel('volume (m^3)')
ylabel('pressure (Pa)')
loglog()
xlim(1e-1,5e0)
ylim(1e5,1e7)
showme()
clf()

plot(V41,U41)
xlabel('Volume (m^3)')
ylabel('Internal Energy (kJ/kg)')

showme()
clf()



from pithy import *

St = {}

#Set States
T1 = 400+273 #K
P1 = 30e5 #Pa
St[1] = stater('T',T1,'P',P1,'water')

T2 = 100+273 #K
x2 = 1
St[2] = stater('T',T2,'Q',x2,'water')

W_measured = 540e3 #J/kg

print state_table(St)


#Calculate Entropy and the figure out the heat loss
print 'h2-h1 = %.2f kJ/kg' % ((St[1]['H'] - St[2]['H'])/1000) 
print 'Energy Lost = %.2f kJ/kg' % ((St[1]['H'] - St[2]['H']-W_measured)/1000)

vel_1 = 160
vel_2 = 100

KE = (vel_2**2)/2 - (vel_1**2)/2
print 'KE Drop = %.2f kJ/kg' % (KE/1000)
Qcv_m = ((St[2]['H'] - St[1]['H']+W_measured)/1000) + KE/1000
print 'Heat Lost = %.2f kJ/kg' % Qcv_m


#Knowing Tb, find the entropy production
Tb = 350 #K
sgen = Qcv_m/Tb + (St[2]['S']-St[1]['S'])/1000
print 'entropy generated = %.2f kJ/(K kg)' % sgen


figure(figsize=(10,5))
#Plot Stuff
subplot(1,2,1)
ts_phase_envelope('water')
Ts = []
ss = []
for i in range(1,3):
    Ts.append(St[i]['T'])
    ss.append(St[i]['S'])
    annotate(str(i),xy=(ss[-1],Ts[-1]))
plot(ss,Ts,'r')
xlim(6000,8000)
xlabel("Entropy (J/(kg K))")
ylabel("Temperature (K)")

subplot(1,2,2)
pv_phase_envelope('water')
ps = []
vs = []
for i in range(1,3):
    ps.append(St[i]['P'])
    vs.append(St[i]['V'])
    annotate(str(i),xy=(vs[-1],ps[-1]))
plot(vs,ps,'r')
xlabel("Volume (m^3/(kg))")
ylabel("Pressure (Pa)")
loglog()
xlim(1e-2,1e1)
showme()
clf()
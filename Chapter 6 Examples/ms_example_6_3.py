from pithy import *

St = {}

P2 = 827371 #120 PSi to Pa
x1 = 1


T1 = 261 #10 F to K

St[1] = stater('T',T1,'Q',x1,'R134a')
s2 = St[1]['S']  #Adiabatic and reversible s1 = s2 
St[2] = stater('P',P2,'S',s2,'R134a')


print state_table(St)


delta_u_table =  St[2]['U'] - St[1]['U']
W_over_m = -delta_u_table

delta_s = St[2]['S']-St[1]['S'] #no heat added, all irreversible entropy

print "The work done on the system is %.0f kJ/kg" % (W_over_m/1000)
print "The entropy generated by the system is %.3f kJ/kg" % (delta_s/1000)


figure(figsize=(10,5))
#Plot Stuff
subplot(1,2,1)
ts_phase_envelope('R134a')
Ts = []
ss = []
for i in range(1,3):
    Ts.append(St[i]['T'])
    ss.append(St[i]['S'])
    annotate(str(i),xy=(ss[-1],Ts[-1]))
annotate("Not Q/m",xy=(4500,200),ha="center")
plot(ss,Ts,'r')

xlabel("Entropy (J/(kg K))")
ylabel("Temperature (K)")

subplot(1,2,2)
pv_phase_envelope('R134a')
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
xlim(1e-4,1e1)
showme()
clf()
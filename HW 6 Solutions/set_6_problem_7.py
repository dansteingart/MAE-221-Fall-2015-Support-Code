from pithy import *

St = {}
Pl = [1e6,2e4,2e4,1e6]
xl = [1,.88,.18,0]

#check possibility of operation
def possible(v):
    if v == 0: return "possible and reversible"
    elif v >0: return "possible and irreversible"
    else:      return "impossible"


for i in range(4): St[1+i] = stater('P',Pl[i],'Q',xl[i],'water')

print state_table(St)

W_turbine = -(St[2]['H']-St[1]['H'])
W_pump    = -(St[4]['H']-St[3]['H'])
Q_in      =  (St[1]['H']-St[4]['H'])
Q_out     =  (St[3]['H']-St[2]['H'])

W_cycle = W_turbine + W_pump

eta = W_cycle/Q_in
print "The Process Efficiency is %.2f" % eta
eta_carnot = 1 - St[2]['T']/ St[1]['T']
print "The Carnot Efficiency is %.2f" % eta_carnot

print "The Cycle is ", possible(eta_carnot-eta)

#Let's examine the Pump
S_pump    = (St[4]['S']-St[3]['S'])
print "The stated pump operation is ", possible(S_pump)

#Let's examine the Trubine
S_turbine    = (St[2]['S']-St[1]['S'])
print "The stated turbine operation is ", possible(S_turbine)

#Plot Stuff
ts_phase_envelope('water')
Ts = []
ss = []
for i in range(1,5):
    Ts.append(St[i]['T'])
    ss.append(St[i]['S'])
Ts.append(Ts[0])
ss.append(ss[0])
plot(ss,Ts,'r')
xlabel("Entropy (J/(kg K))")
ylabel("Temperature (K)")
showme()
clf()
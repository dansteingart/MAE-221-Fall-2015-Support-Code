from pithy import *

St = {}

#Set States
T1 = 273-5 #K
p1 = 3.5e5 #Pa
St[1] = stater('T',T1,'P',p1,'R22')

T2 = 75+273 #K
p2 = 14e5   #Pa
St[2] = stater('T',T2,'P',p2,'R22')

T3 = 28+273 #K
p3 = 14e5 #Pa
St[3] = stater('T',T3,'P',p3,'R22')

h4 = St[3]['H'] #J/kg
p4 = p1 #Pa
St[4] = stater('P',p4,'H',h4,'R22')

T5 = 20 + 273. #K
p5 = 1e5 #Pa
St[5] = stater('T',T5,'P',p5,'air')

T6 = 50 + 273. #K
p6 = p5 #Pa
R = 8.314/28.97  # J/kg L
St[6] = stater('T',T6,'P',p6,'air')


AV_air = .42 #m^3/s
mdot_air = AV_air * p5/(R*T5) / 1000
cp_air = 1.005 #kJ/kj K
print state_table(St)

#Condenser
#first solve for m_r22
mdot_r22 = mdot_air*cp_air*(T6-T5)/((St[2]['H']-St[3]['H'])/1000)

#Assume for all devices Q dot = 0
#now, solve for entropy created 
sigma_air = cp_air*log(T6/T5) #kJ/(kg K)
sigma_r22_cond = (St[3]['S']-St[2]['S'])/1000  #kJ/(kg K)
sigmadot_cond = mdot_air*sigma_air+mdot_r22*sigma_r22_cond # kW/K

#Compressor in kW/K
sigmadot_comp = mdot_r22 * (St[2]['S']-St[1]['S'])/1000

#Valve in kW/K
sigmadot_valve = mdot_r22 * (St[4]['S']-St[3]['S'])/1000

#Print the results in kW/k
results = whos(locals(),pattern="poof")  # trick to stop whos() from printing while returning result set as dictionary

#Now just pull out the sigmadots
keys = []
for k in results.keys():
    if k.find("sigmadot") > -1: keys.append(k)

#Sort by magnitude of entropy in increasing order, and reverse)
losses = sorted(keys,key = lambda k: results[k])
losses.reverse()

#Print in order of decreasing losses.
for l in losses:
    print "%s = %.6f kW/k" % (l,results[l])

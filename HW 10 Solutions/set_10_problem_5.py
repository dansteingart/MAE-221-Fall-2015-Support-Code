from pithy import *

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv + R_air

cpr = 10

#Before Diffuser
AV1 = 83.7 # m^3/s
P1 = 40e3  # Pa 
T1 = 240   # K
vel1 = 180 # m/s
mdot = (AV1*P1/(R_air*T1))/1000 #kg/s

#After Diffuser
vel2 = 0 # m/s
#first law balance
# 0 = Qdot + Wdot + mdot (hi + veli^/2) - mdot (he + vel^/2)

# cold standard analysis cp dT = dh
# cp (T2-T1) = Vel^2/2
T2 = (vel1**2/2)/(cp*1000) + T1 #K
P2 = P1*(T2/T1)**(k/(k-1)) # Pa

#2-3 Compressor 
eta_comp = 0.85 
cpr = 10
P3 = P2 * 10 # Pa
T3s = T2*((P3/P2)**((k-1)/k)) #K
T3 = T2+(T3s-T2)/eta_comp #K

#3-4 Combustor
T4 = 1140 #K
P4 = P3 # Pa

#4-5 Turbine
eta_turb = 0.85
P5 = 50e3 #Pa
T5s = T4*((P5/P4)**((k-1)/k)) #K
T5 = T4-(T4-T5s)*eta_comp #K

#5-6 Nozzle, same analysis as states 1-2
P6 = P1 # atmosphere
T6 = T5*((P6/P5)**((k-1)/k))
vel6 = sqrt(2*cp*(T5-T6)*1000) #m/s

Ps = [P1,P2,P3,P4,P5,P6]
Ts = [T1,T2,T3,T4,T5,T6]

print "<table style='font-size:14px'><tr><td>State</td><td style='width:100px'>T (K)</td><td>P (kPa)</td></tr>",
for i in range(len(Ts)):
    print "<tr><td>%i</td><td>%.2f</td><td>%.2f</td></tr>" % (i+1,Ts[i],Ps[i]/1000),
print "</table>"
    

Wdotcomp = mdot*cp*(T3-T2)
Wdotturb = mdot*cp*(T4-T5)
Wdotnet = Wdotturb-Wdotcomp

print "Part a) The power to the propellor is %.2f kW" % Wdotnet
print "Part b) The velocity at the nozzle exit is %.2f m/s" % vel6

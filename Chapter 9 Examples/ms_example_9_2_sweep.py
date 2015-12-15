from pithy import *



R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv + R_air

r = 18.  #V1/V2
rc = 2.  #V3/V2, cut off ratio or when fuel addition "cuts off"

figure(figsize=(12,12))
for r in [10.,15.,18.,20.]:
    T1 = 300 #K
    P1 = 1e5 #Pa
    
    T2 = T1*exp(-(R_air/cv)*log(1/r))
    P2 = P1*(T2/T1 *(r))
    
    P3 = P2
    T3 = T2*rc
    
    T4 = T3*(rc/r)**(k-1)
    P4 = P1*T4/T1
    
    Q_C = cv*(T4-T1)
    Q_H = cp*(T3-T2)
    
    eta = 1 - Q_C/Q_H

    W_cycle = Q_H - Q_C
    
    
    v1 = R_air*T1/P1 * 1000 

    MEP = W_cycle/v1

    v2 = R_air*T2/P2 * 1000 
    v3 = R_air*T3/P3 * 1000 
    v4 = R_air*T4/P4 * 1000 
    
    s1 = 0
    s2 = s1
    s3 = s2+cv*log(T3/T2)+R_air*log(v3/v2)
    s4 = s3
    
    Ps = [P1,P2,P3,P4,P1]
    vs = [v1,v2,v3,v4,v1]
    Ts = [T1,T2,T3,T4,T1]
    ss = [s1,s2,s3,s4,s1]
    
    subplot(2,1,1)
    title("The Effect of Changing Cutoff Ratio (r)")
    plot(vs,Ps,alpha=.5,label="r = %.0f, eta = %.2f, MEP =  %.0f kPa, W_cycle = %.0f kJ/kg"%(r,eta,MEP,W_cycle),linewidth=2)
    legend(loc="best",frameon=False)
    xlabel("Volume (m^3/kg)")
    ylabel("Pressure (kPa)")
    semilogy()
    ylim(8e4,2e7)
    subplot(2,1,2)
    plot(ss,Ts,alpha=.5,label="r = %.1f, rc = %.1f" %(r,rc),linewidth=2)
    ylabel("Temperature (K)")
    xlabel("Entropy (kJ/kg K) vs. state 1")
    xlim(-.1,.8)
showme()
clf()

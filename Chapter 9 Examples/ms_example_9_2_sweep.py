from pithy import *



R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv + R_air

r = 18.  #V1/V2
rc = 2.  #V3/V2, cut off ratio or when fuel addition "cuts off"

figure(figsize=(10,10))
crs = [10.,15.,18.,25.] 
for r in crs:
    T1 = 300 #K
    P1 = 1e5 #Pa
    
    T2 = T1*exp(-(R_air/cv)*log(1/r))
    r12 = linspace(1,r,100)
    T12 = T1*exp(-(R_air/cv)*log(1/r12))

    P2 = P1*(T2/T1 *(r))
    P12 = P1*(T12/T1 *(r12))
    P3 = P2
    T3 = T2*rc
   
    v1 = R_air*T1/P1 * 1000 
    v2 = R_air*T2/P2 * 1000 
    v3 = R_air*T3/P3 * 1000 
        
    T4 = T3*(rc/r)**(k-1)
    P4 = P1*T4/T1
    v4 = R_air*T4/P4 * 1000  
    r34 = linspace(1,v4/v3,100)
    T34 = T3*exp(-(R_air/cv)*log(r34))
    P34 = P3*(T34/T3 *(1/(r34)))

    

    Q_C = cv*(T4-T1)
    Q_H = cp*(T3-T2)
    
    eta = 1 - Q_C/Q_H

    W_cycle = Q_H - Q_C
    MEP = W_cycle/v1
    
    

    v12 = R_air*T12/P12 * 1000 
    #v34 = R_air*T34/P34 * 1000 

    s1 = 0
    s2 = s1
    s3  = s2+cv*log(T3/T2)+R_air*log(v3/v2)
    T23 = linspace(T2,T3,100)
    v23 = linspace(v2,v3,100)
    s23 = s2+cv*log(T23/T2)+R_air*log(v23/v2)
    
    s4 = s3
    T41 = linspace(T4,T1,100)
    v41 = linspace(v4,v1,100)
    s41 = s2+cv*log(T41/T2)+R_air*log(v41/v2)
    v34 = linspace(v3,v4,100)
    Ps = [P1,P2,P3,P4,P1]
    vs = [v1,v2,v3,v4,v1]
    # Ts = [T1,T2,T3,T4,T1]
    # # ss = [s1,s2,s3,s4,s1]
    Ts = concatenate(([T1],T23,T41))
    ss = concatenate(([s1],s23,s41))
    Ps = concatenate((P12,P34,[P1]))
    vs = concatenate((v12,v34,[v1]))
    
    subplot(2,1,1)
    title("Diesel Cycle: Effect of a Changing Compression Ratio (r),(rc = %.1f)" % rc)
    plot(vs,Ps,alpha=.5,label="r = %.0f, eta = %.2f, MEP =  %.0f kPa, W_cycle = %.0f kJ/kg"%(r,eta,MEP,W_cycle),linewidth=2)
    if r == crs[3]: #if first sweep, annotate plot
        annotate("1",xy=(v1,P1))
        annotate("2",xy=(v2,P2))
        annotate("3",xy=(v3,P3))
        annotate("4",xy=(v4,P4))

    legend(loc="best",frameon=False)
    xlabel("Volume (m^3/kg)")
    ylabel("Pressure (kPa)")
    semilogy()
    ylim(8e4,2e7)
    subplot(2,1,2)
    plot(ss,Ts,alpha=.5,label="r = %.1f, rc = %.1f" %(r,rc),linewidth=2)
    if r == crs[3]: #if first sweep, annotate plot
        annotate("1",xy=(s1,T1))
        annotate("2",xy=(s2,T2))
        annotate("3",xy=(s3,T3))
        annotate("4",xy=(s4,T4))

    ylabel("Temperature (K)")
    xlabel("Entropy (kJ/kg K) vs. state 1")
    xlim(-.1,.8)
showme()
clf()

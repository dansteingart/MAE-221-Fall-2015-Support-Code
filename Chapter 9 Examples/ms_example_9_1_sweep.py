from pithy import *

#Using air standard "cold" analysis, see comparison in MS 8e pg. 517 

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air
k = 1.4
cv = R_air/(k-1)
cp = cv+R
r = 8.0 #compression ratio

TC = 540 * .55 # K
TH = 3600 * .55 # K
figure(figsize=(9,9))

for r in [5.,8.,10.,15.]:
    T1 = TC
    P1 = 1e5
    V1 = 0.0005663369 # m^3
    
    T2 = T1*exp(-(R_air/cv)*log(1/r))
    P2 = P1*T2/T1 *(r)

    r12 = linspace(1,r,100)
    T12 = T1*exp(-(R_air/cv)*log(1/r12))
    P12 = P1*(T12/T1)*(r12)
    
    #2 to 3, cv heating 
    Qin = 931
    T3 = Qin/cv + T2
    #T3 = TH
    P3 = P2*T3/T2 
    
    #3 to 4, isentropic expansion
    T4 = T3*exp(-(R_air/cv)*log(r))
    P4 = (P3)*(T4/T3)*(1/r)
    
    r34 = linspace(1,r,100)
    T34 = T3*exp(-(R_air/cv)*log(r34))
    P34 = P3*(T34/T3)*(1/r34)

    Q41 = cv*(T4-T1)
    Q23 = cv*(T3-T2)
    eta = 1 - (Q41/Q23)
    
    mass = P1*V1/(R_air*T1)
    Wcycle = mass*(Q23-Q41)
    mep = Wcycle/(V1*(1-(1/r))) 
    
    #PV = mRT
    V2 = mass*R_air*T2/P2
    V3 = V2
    V4 = V1
    
    V12 = mass*R_air*T12/P12
    V34 = mass*R_air*T34/P34

    S1 = 0
    S2 = S1
    S3 = S2 + mass*(cp*log(T3/T2)-R_air*log(P3/P2))
    S4 = S3 

    T23 = linspace(T2,T3,100)
    P23 = linspace(P2,P3,100)
    S23 = S2 + mass*(cp*log(T23/T2)-R_air*log(P23/P2))
    
    T41 = linspace(T4,T1,100)
    P41 = linspace(P4,P1,100)
    S41 = S4 + mass*(cp*log(T41/T4)-R_air*log(P41/P4))
    

    # Ps = [P1,P2,P3,P4,P1]
    # Vs = [V1,V2,V3,V4,V1]
    # Ts = [T1]+[TT3,T4,T1]
    # Ss = [S1,S2,S3,S4,S1]
    Ps = concatenate((P12,[P3],P34,[P1]),0)
    Vs = concatenate((V12,[V3],V34,[V1]),0)
    Ts = concatenate(([T1,T2],T23,[T3,T4],T41),0)
    Ss = concatenate(([S1,S2],S23,[S3,S4],S41),0)

    subplot(2,1,1)
    plot(Vs,Ps,label="r = %.0f, eta = %.2f, MEP =  %.1f kPa, W_cycle = %.0f kJ/kg" % (r,eta,mep/1e5,Wcycle))
    semilogy()
    title("The Effect of Changing Compression Ratio (r)")
    ylabel("Pressure (Pa)")
    xlabel("Volume (m^3)")
    ylim(5e4,2e7)
    legend(loc='best',fontsize=11,frameon=False)
    subplot(2,1,2)
    plot(Ss,Ts)
    xlim(-1,8)
    ylabel("Temperature (K)")
    xlabel("Entropy vs. State 1 (kJ/K)")

showme()
clf()


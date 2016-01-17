from pithy import *

#The Atkinson cycle is a modification to the air standard Otto cycle where the constant volume heat rejection step is replace with a constant pressure heat rejection step.  See the figure below


#For the both cycles, using cold air standard analysis of air where Mair = 28.97 g/mol and R = 8.31446 J/(mol K), and k = 1.4

# if p1 = 1 Bar, T1 = 300 K, and Q23/m = 2000 kJ/kg

# Determine T, s (vs. state 1), P and v and present a table for both cycles using the second law and sketch/plot the TS diagram for both cycles on the same plot

# (b) Evaluate the ratio of the thermal efficiency of the Atkinson cycle, 1-2-3-4-1, to the thermal efficiency of the Otto cycle, where for the Otto cycle v4' = v1 and for the Atkinson Cycle p4 = p1

# (c) Evaluate the ratio of the mean effective pressure of the Atkinson cycle to the mean effective pressure of the Otto cycle.

from pithy import *

#Using air standard "cold" analysis, see comparison in MS 8e pg. 517 

R = 8.31415 # J/(mol K)
M_air = 28.97 # g/mol
R_air = R/M_air #J/(g K)
k = 1.4
cv = R_air/(k-1) #J/(g K)
cp = cv+R_air #J/(g K)

r = 8.0 #compression ratio
TC = 300 # K
Qin = 2000 #kJ/kg

figure(figsize=(9,9)) #Set figure size


for c in ['o','a']:
    if c == 'a': mp = '--'
    else: mp = 'r-'

    #Starting Conditions
    T1 = TC
    P1 = 1e5
    V1 = 0.0005663369 # m^3
    mass = P1*V1/(R_air*T1)
    
    #1-2 Isentropic Heating
    T2 = T1*exp(-(R_air/cv)*log(1/r))
    P2 = P1*T2/T1 *(r)
    
    V2 = mass*R_air*T2/P2
    
    #2 to 3, CV heating 
    Q23 = Qin
    T3 =  T2+(Q23/cv)
    V3 = V2
    P3 = mass*R_air*T3/V3

    if c == 'o':
        #3 to 4, isentropic expansion
        V4 = V1
        T4 = T3*exp(-(R_air/cv)*log(V4/V3))
        P4 = (P3)*(T4/T3)**(k/(k-1))
    
    if c == 'a':
        #3 to 4, isentropic expansion
        P4 = P1
        T4 = T3*(P4/P3)**((k-1)/k)
        V4 = mass*R_air*T4/P4
    
    #V4 = V1
    
    #Calculate Heats/Work
    if c == 'o': Q41 = cv*(T4-T1)
    if c == 'a': Q41 = cp*(T4-T1)
    
    S1 = 0
    S2 = S1
    S3 = S2 + mass*(cp*log(T3/T2)-R_air*log(P3/P2))
    S4 = S3 
    
    Ps = [P1,P2,P3,P4,P1]
    Vs = [V1,V2,V3,V4,V1]
    Ts = [T1,T2,T3,T4,T1]
    Ss = [S1,S1,S3,S4,S1]
    
    eta = 1 - (Q41/Q23)
    Wcycle = mass*(Q23-Q41)
    mep = Wcycle/(max(Vs)-min(Vs)) 


    subplot(2,1,1)
    plot(Vs,Ps,mp,label="r = %.0f, eta = %.2f, MEP =  %.1f kPa, W_cycle = %.0f kJ/kg" % (r,eta,mep/1e5,Wcycle))
    for i in range(4):
        st = str(i+1)
        if st == "4": st = st+c
        annotate(st,xy=(Vs[i],Ps[i]))
    loglog()

    title("Comparison: Atkinson Vs. Otto")
    ylabel("Pressure (Pa)")
    xlabel("Volume (m^3)")
    ylim(5e4,3e7)
    legend(loc='best',fontsize=11,frameon=False)
    
    subplot(2,1,2)
    plot(Ss,Ts,mp)
    for i in range(4):
        st = str(i+1)
        if st == "4": st = st+c
        annotate(st,xy=(Ss[i],Ts[i]))
    xlim(-.1,1)
    ylabel("Temperature (K)")
    xlabel("Entropy vs. State 1 (kJ/K)")
    semilogy()

showme()
clf()

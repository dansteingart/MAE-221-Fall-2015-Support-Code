from pithy import *

AV1 = 5  # m^3/s
P1 = 1e5 # Pa
T1 = 300 # K
Rair = 8.31446 / 28.97 #kJ/(kg K)

#use cold air standard

k = 1.4
cv = Rair/(k-1) 
cp = cv+R

mdot = AV1*P1/(Rair*T1)/1000 #kg/s


cprs = [6.,8.,12.]

print "Assume Cold Standard"
print

for cpr in cprs:
    print "For a compressor pressure ratio of %i" % cpr

    #Through Compressor
    P2 = P1 * cpr #Pa
    T2 = T1*(cpr)**((k-1)/k)

    #Through Combustor
    T3 = 1400 #K
    P3 = P2
    
    #Through Turbine
    P4 = P1
    T4 = T3*(1/cpr)**((k-1)/k)

    Ps = [P1,P2,P3,P4]
    Ts = [T1,T2,T3,T4]

    print "<table style='font-size:14px'><tr><td>State</td><td style='width:100px'>T (K)</td><td>P (kPa)</td></tr>",
    for i in range(len(Ts)):
        print "<tr><td>%i</td><td>%.2f</td><td>%.2f</td></tr>" % (i+1,Ts[i],Ps[i]/1000),
    print "</table>"
    
    Qdotin  = mdot*cp*(T3-T2)
    Qdotout = mdot*cp*(T4-T1)
    
    eta = 1 - Qdotout/Qdotin
    
    print 'eta = 1 - Qdotout/Qdotin =  %.2f' % eta

    Wdotcomp = mdot*cp*(T2-T1)
    Wdotturb = mdot*cp*(T3-T4)
    
    bwr = Wdotcomp/Wdotturb
    
    print 'bwr = Wdotcomp/Wdotturb = %.2f' % bwr

    Wdotnet = Wdotturb - Wdotcomp 

    print "Wdotnet = Wdotturb - Wdotcomp = %.2f kW" % Wdotnet
    print

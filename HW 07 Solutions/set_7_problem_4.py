from pithy import *
#Problem P6.95
#Figure P6.95 provides steady-state test data for a control volume in which two entering streams of air mix to form a single exiting stream. Stray heat transfer and kinetic and potential energy effects are negligible. A hard-to-read photocopy of the data sheet indicates that the pressure of the exiting stream is either 1.0 MPa or 1.8 MPa. Assuming the ideal gas model for air with cp = 1.02 kJ/(kg K), determine if either or both of these pressure values can be correct.

print "<center><img style='width:600px;' src='http://steingart.princeton.edu:8002/static/realfiles/mae221fall2015/ss_1447619308.png'></center>"
M_air = 28.97
R = 8.314
R_air = R/M_air
cp = 1.02 #kJ/(kg K) 

T1    = 800.  #K
p1    = 18e5 #Pa
m1dot = 1    #kg/s

T2    = 650.  #K
p2    = 10e5 #Pa
m2dot = 2    #kg/s

#First find T3

# 0 = Qcv - Wcv + sum(mi hi) - sum(me he)

# 20151129 Added steps below for clarificaiton, answer is still the same
# 0 = m1dot * h1 + m2dot*h2 - m3dot * h3
# m3dot = m1dot + m2dot
# m1dot * h1 + m2dot*h2 - (m1dot + m2dot) * h3
# m1dot * cp*T1 + m2dot*cp*T2 - (m1dot + m2dot) *cp* T3

T3 = (m1dot*T1 + m2dot*T2)/(m1dot + m2dot)
#Now use the ideal gas model to try  P3 = 1.0 MPa
p3 = 10e5
sigma1 = m1dot*(cp*log(T3/T1) - R_air*log(p3/p1)) + m2dot*(cp*log(T3/T2) - R_air*log(p3/p2))

#Now use the ideal gas model to try P3 = 1.8 MPa
p3 = 18e5
sigma2 = m1dot*(cp*log(T3/T1) - R_air*log(p3/p1)) + m2dot*(cp*log(T3/T2) - R_air*log(p3/p2))


#Print a nice plot showing what's going on (not required for problem but helpful for analysis)
p3 = linspace(8e5,20e5,100)
sigma = m1dot*(cp*log(T3/T1) - R_air*log(p3/p1)) + m2dot*(cp*log(T3/T2) - R_air*log(p3/p2))
p_max = p3[abs(sigma).argmin()]/1e6
fill_between([0.8,p_max],-.5,.4,color="g",alpha=.3)
fill_between([p_max,2],-.5,.4,color="r",alpha=.3)
annotate("possible",xy=(.9,0.1))
annotate("Pressure 1\n 1.0 MPa",xy=(1,sigma1))
annotate("Pressure 2\n 1.8 MPa",xy=(1.8,sigma2))
annotate("impossible",xy=(1.4,0.1))
plot(p3/1e6,sigma,'purple')
plot([1,1.8],[sigma1,sigma2],'ko')
axvline(p_max,color=".1")
#axhline(0,color=".1")
ylim(-.5,.4)
xlabel("Pressure (MPa)")
ylabel("Entropy Generated (kJ/(K kg))")

showme()
clf()

print "An output pressure of 1 MPa is possible, an output pressure of 1.8 MPa is impossible"

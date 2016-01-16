from pithy import *

"""2.33 A gas contained within a piston-cylinder assembly 
undergoes three processes in series:

Process 1-2: Constant volume from p1 = 1 bar, V1 = 4 m to state 2, where p2 =2 bar.

Process 2-3: Compression to V3 = 2 m during which the pressure-volume relationship is pV = constant.

Process 3-4: Constant pressure to state 4, where V4 = 1 m3

Sketch the processes in series on pV coordinates and 
evaluate the work for each process, in kJ.

"""

P1 = 1e5 #Pa
V1 = 4 # m^3

P2 = 2e5 #Pa
V2 = V1
P12 = linspace(P1,P2,10)
V12 = linspace(V1,V2,10)

c = P2*V2 #= P3*V3
V3 = .5 * V2 
V23 = linspace(V2,V3,100)
P3 = c/V3
P23 = c/V23
P4 = P3
V4 = .5 * V3
P34 = linspace(P3,P4,10)
V34 = linspace(V3,V4,10)

P = [P1,P2,P3,P4]
V = [V1,V2,V3,V4]


plot(V,P,'.')
plot(V12,P12,'r')
plot(V23,P23,'r')
plot(V34,P34,'r')
xlim(0,5)
ylim(0,5e5)
ylabel("Pressure (Pa")
xlabel("Volume (m^3")
showme()
clf()

W12 = 0
W23 = integrate.simps(P23,V23)
W34 = integrate.simps(P34,V34)

print "The work associated with process W12 is %.2e J" % W12
print "The work associated with process W23 is %.2e J" % W23
print "The work associated with process W34 is %.2e J" % W34


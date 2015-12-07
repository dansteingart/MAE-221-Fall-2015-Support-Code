from pithy import *

R = 8.31446/28.97 # (J/g K)
n = 1.19

k  = 1.4
cv = R/(k-1)
cp = k*R/(k-1)

P1 = 1. # Bar
P2 = 5 # Bar
P3 = 1. # Bar

T1 = 290. # K
T2 = T1*(P2/P1)**((n-1)/n) # K 

v1 = R*T1/P1
v2 = R*T2/P2
v3 = 67.9 #m^3/kg

delS12 = cv*log(T2/T1)+R*log(v2/v1) #the system _loses_ entropy to the environment
delS23 = 0 #isentropic

#for sketching purposed set S1 to something arbitrary

S1 = abs(delS12)*2
S2 = S1 + delS12
S3 = S2 - delS23

#solve for T3 => 0 = cv*log(T3/T2)+R*log(v3/v2)
T3 = exp(-R*log(v3/v2)/cv)*T2

S = [S1,S2,S3]
T = [T1,T2,T3]

print "<h3>Part A: Sketch</h3>"
plot(S,T,'r')
for i in range(3):
    annotate(str(i+1),xy=(S[i],T[i]))
xticks([])
yticks([])
xlabel("Entropy (J/K kg)")
ylabel("Temperature (K)")
xlim(0,.5)
ylim(200,400)
showme()
clf()

print "<h3>Part B: Temperatures</h3>"
print "T2 = T1*(P2/P1)**((n-1)/n) =", round(T2,2) ,"K"
print "solve for T3 => 0 = cv*log(T3/T2)+R*log(v3/v2)"
print "T3 = exp(-R*log(v3/v2)/cv)*T2 =", round(T3,2) ,"K"


print "<h3>Part C: Work</h3>"
W12 = R*(T2-T1)/(1-n)
print "W12 = R*(T2-T1)/(1-n) =",round(W12,1),"kJ/kg"
W23 = -cv*(T3-T2)
print "W23 = -cv*(T3-T2) =",round(W23,1),"kJ/kg"
Wnet = W23 + W12
print "Wnet = W23 + W12 =",round(Wnet,1),"kJ/kg"


print "<h3>All Variables</h3>"
whos(locals())

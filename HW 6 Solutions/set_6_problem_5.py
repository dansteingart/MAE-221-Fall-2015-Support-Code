from pithy import *

TH = 1800.
TC = 600.

eta_max = 1-TC/TH

def check():
    if Qh-Qc == Wcycle:
        if (1-Qc/Qh) > eta_max: return "impossible" #fails the second law balance
        elif (1-Qc/Qh) == eta_max: return "reversible" #ideal process
        else: return "irreversible" #entropy generating process
    else: return "impossible" #fails the first law balance

#Case A 
Qc = 100.
Qh = 500.
Wcycle = Qh-Qc
print "Case A is", check()

#Case B
Qc = 200.
Wcycle = 250.
Qh = 500.
print "Case B is", check()

#Case C
Wcycle = 350.
Qc = 150.
Qh = Qc+Wcycle
print "Case C is", check()

#Case D
Qc = 200.
Qh = 500.
Wcycle = Qh-Qc
print "Case D is", check()

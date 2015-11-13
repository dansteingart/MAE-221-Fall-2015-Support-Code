from pithy import *

TH = 1800.
TC = 600.

eta_max = 1-TC/TH

def check():
    if (1-Qc/Qh) > eta_max: return "impossible"
    elif (1-Qc/Qh) == eta_max: return "reversible"
    else: return "irreversible"

def check2():
    if Qh-Qc == Wcycle: check()
    else: return "impossible"


#Case A 
Qc = 100.
Qh = 500.
print "Case A is", check()

#Case B
Qc = 200.
Wcycle = 250.
Qh = 500.
print "Case B is", check2()

#Case C
Wc = 350.
Qc = 150.
Qh = Qc+Wc
print "Case C is", check()

#Case D
Qc = 200.
Qh = 500.
print "Case D is", check()
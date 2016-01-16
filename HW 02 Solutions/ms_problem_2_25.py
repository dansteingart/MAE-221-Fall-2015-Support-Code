from pithy import *
from scipy import optimize

"""Measured data for pressure versus volume during the 
expansion of gases within the cylinder of an internal 
combustion engine are given in the table below. Using data 
from the table, complete the following:
(a) Determine a value of n such that the data are fit by an 
equation of the form, pV
n
5 constant.
(b) Evaluate analytically the work done by the gases, in kJ, 
using Eq. 2.17 along with the result of part (a).
(c) Using graphical or numerical integration of the data, 
evaluate the work done by the gases, in kJ.
(d) Compare the different methods for estimating the work 
used in parts (b) and (c). Why are they estimates?

"""


P = [15,12,9,6,4,2] #Bar
V = [300,361,459,644,903,1608] #cm^3

P = array(P) * 100 # to kPa
V = array(V) * 1e-6 #m^3

n_guess = 1

def Vol(P_hold,n_hold): 
    return ((P[0]*V[0]**n_hold)/P_hold)**(1/n_hold)


n = optimize.curve_fit(Vol,P,V,n_guess)[0]


Ps = linspace(P[0],P[-1],100)

W_analytical = (P[-1]*V[-1]-P[0]*V[0])/(1-n)
W_comp = integrate.simps(P,V)

plot(P,V,'bo-')
plot(Ps,Vol(Ps,n),'r')
#1print dir(mpld3)
ylabel("V (m^3)")
xlabel("Pressure (kPa)")
showme()
clf()

whos(locals())

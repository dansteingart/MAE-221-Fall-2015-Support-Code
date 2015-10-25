from pithy import *

"""In a heat-treating process, a 1-kg metal part, initially at 1075 K, is quenched in a closed tank containing 100 kg of water, initially at 295 K. There is negligible heat transfer between the contents of the tank and their surroundings. Modeling the metal part and water as incompressible with constant specific heats 0.5 kJ/kg-K and 4.4 kJ/kg-K, respectively, determine the final equilibrium temperature after quenching, in K.

"""


m_metal = 1 #kg
m_water = 100 #kg
Ti_water = 295 #K
Ti_metal = 1075 #k
c_metal =0.5 #kJ/kg K
c_water = 4.4 #kJ/kg K

#Tf = Tf_water = Tf_metal
#c_metal*m_metal(Tf - Ti_metal) = - c_water*m_water(Tf - Ti_water)

Tf = (c_metal*m_metal*Ti_metal + c_water*m_water*Ti_water)/(c_metal*m_metal + c_water*m_water)

print "The final Temperature is ",round(Tf,1),"K"


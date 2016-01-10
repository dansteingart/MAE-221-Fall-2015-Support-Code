from pithy import *

T = 273+600 
P = 8e5

St = {}

St[1] =  stater('P',P,'T',T,'water')



#First set a target quality
x_target = 0.9 

#First we set up a range of pressures to test over. 
ptest = logspace(0,5,100) #1 to 1e5, 100 points.

#This line finds the pressure in that range that gets us closest to the target quality
P2 = ptest[abs(stater('S',St[1]['S'],'P',ptest,'water')['Q']-x_target).argmin()] #find closest pressure

#Set the State
St[2] =  stater('S',St[1]['S'],'P', P2,'water') #set state

print state_table(St)



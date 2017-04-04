#Graphing problem 1 for Astr3002 Hw8
#Jenny Calahan
#Oct 24th, 2016

import matplotlib.pyplot as plt
import numpy as np
import pylab
import matplotlib.patches as mpatches



theta = np.arange(0, 90, 0.1)
B_app_2 = []
B_app_4 = []
B_app_5 = []
B_app_7 = []
B_app_10 = []
B_app_half = []


def B_obs(L,i):
    return (B(L)*np.sin(np.deg2rad(theta[i])))/(1-B(L)*np.cos(np.deg2rad(theta[i])))

def B(L):
    return 1/(np.sqrt(1-(1./L)))



for j in range(len(theta)): 
    B_app_2.append(B_obs(2,j))
    B_app_4.append(B_obs(4,j))
    B_app_5.append(B_obs(5,j))
    B_app_7.append(B_obs(7,j))
    B_app_10.append(B_obs(10,j))
    B_app_half.append(B_obs(4./3.,j))
'''
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Apparent velocity vs Theta')
ax.set_xlabel('Theta (degrees) ')
ax.set_ylabel('Beta (v/c)') 
ax.set_ylim([-20,20])
    

plt.plot(theta, B_app_2,'r^',label= 'Lorentz Factor 2')
plt.plot(theta, B_app_4,'b^',label='Lorentz Factor 4')
plt.plot(theta, B_app_5,'m^',label= 'Lorentz Factor 5')
plt.plot(theta, B_app_7,'g^',label= 'Lorentz Factor 7')
plt.plot(theta, B_app_10,'c^',label= 'Lorentz Factor 10')
plt.plot(theta, B_app_half,'y^',label= 'B is .5')


plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()
'''

B_Bt=[]

def B_ofBt(B_t,i):
    return B_t/(B_t*np.cos(np.deg2rad(theta[i]))+np.sin(np.deg2rad(theta[i])))

for j in range(len(theta)): 
    B_Bt.append(B_ofBt(8.13,j))

low=99
for k in range(len(B_Bt)):
    if B_Bt[k]<low:
        low=B_Bt[k]
        num=k

print(theta[num])                #theta value where B_Bt is lowest
print(low)

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Beta vs Theta where B_t is 8.13')
ax.set_xlabel('Theta (degrees) ')
ax.set_ylabel('Beta ') 
ax.set_ylim([.98,1.0])
ax.set_xlim([0,20.0])
plt.plot(theta, B_Bt,'g')
plt.show()


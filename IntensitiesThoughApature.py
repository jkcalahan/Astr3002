#Graph the intensity of an image after going through a thing with lens and apature
#Jenny Calahan
#Oct 27, 2016

import numpy as np
from scipy.special import j1,j0        #Jinc function?
import matplotlib.pyplot as plt
from scipy.optimize import minimize as mini

v = np.arange(-10, 10, .01)
y = np.arange(-10, 10, .01)
I1 = []
I2 = []
I  = []
x = []

def intensity(wave,W,d,x_0,I_0,k,v):
    part1= I_0*(-1./(wave*d))*(np.exp(2*k*d))*(-1./(wave))*(np.exp(2*k))*(np.exp((2*np.pi*wave*v**2)))
    #part1= I_0*(1./(wave*d))*(1./(wave))
    part2a= (-W*np.sinc(W*v+W*(x_0/(wave*d))))
    part2b= (-W*np.sinc(W*v-W*(x_0/(wave*d))))
    slit1=part1*part2a**2
    slit2=part1*part2b**2
    both=slit1+slit2
    return slit1,slit2,both


wave=0.5e-6
W=.6
d=6e4
x_0=.0125
v_0=x_0/(wave*d)

k=6e-4
I_0=.020


for j in range(len(v)): 
    x1,x2,xb=intensity(wave,W,d,x_0,I_0,k,v[j])
    I1.append(x1)
    I2.append(x2)
    I.append(xb)

maxi=10
m=0
while v[m]<2.0:
    if I1[m]<maxi:
        I1[m]=maxi
        num=m
    m=m+1

print(2*v_0)             #distance between of maxima of each peak
print(v[num]-v_0)        #half width of one peak
        

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Intensity vs v_x''')
ax.set_xlabel('v_x'' (m) ')
ax.set_ylabel('Intensity') 
#ax.set_xlim([-2.,2.])
#ax.set_ylim([0,5e5])  

#plt.plot(y,x)
#plt.plot([-x_0/(wave*d),-x_0/(wave*d)],[0,1e9],'y-') 
#plt.plot([x_0/(wave*d),x_0/(wave*d)],[0,1e9],'m-')
plt.plot(v, I1,'g-')
plt.plot(v, I2,'b-')
#plt.plot(v, I,'r-')






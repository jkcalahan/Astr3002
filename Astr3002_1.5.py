#Jenny Calahan
#My attempt at problem 1.5 to assignment 1 
#Find the co-moving volume per z interval for a flat universe

import scipy.integrate as integrate
import scipy.special as special
import numpy as np
import scipy.constants as sci


#constants
omega_m=0.3
omega_A=0.7
H_0= 70     #km/(s*Mpc)
w=.1        #angle of field of view

#set up an array to put answers in 
comoving_vol = []
z_range = []


def Vol(z,D_A,H(z)):                   #define volume element that will be integrated
    return (sci.c/H(z))*((1+z)**2)*D_A**2

def H(z):                            #define H as a function of redshift z
    return H_0*((omega_m*(1+z)**3)+omega_A)**(1/2)

def V(Vol,zmin,zmax):              #returns a value for the co-moving volume for range of zmin to zmax
    return w*integrate.quad(Vol,zmin,zmax)

z_1=0         #start at z=0
z_lim=1       #end at z=1
dt=.1         #take small steps dt=.1Gyr
while z_1<=z_lim:    #make arrays of the co-moving volume and z so that we can graph them for limits z_1 through z_lim
      comoving_vol.append(V(Vol,z,z+dt))
      z_range.append(z)
      z_1=z+1












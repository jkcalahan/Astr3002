#Calculated the time since the big bang at a certain redshift 
#User gives z, omega_m, omega_rho, and omega_lambda
#Assumes hubble constant is 70 km/s/Mpc

z = 6.0
omega_m      = 0.3
omega_rho    = 0.0
omega_l      = 0.7

def time(z,o_m,o_rho,o_l):
    f = lambda a: ((o_m/a)+(o_rho/(a**2))+(o_l*(a**2)))**(-1/2)
    num, err =integrate.quad(f, 0, (1./(z+1))) 
    return ((num*(1./70.)*3.086e+19)/(3.15e7))/1e9



print(time(z,omega_m,omega_rho,omega_l))


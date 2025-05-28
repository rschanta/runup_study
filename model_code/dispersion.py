import numpy as np
from scipy.optimize import brentq


'''
Tools for solving and plotting the dispersion relation
\sigma^2 = gk\tanh kh

'''
def linear_dispersion(T = None, sigma = None,
                      L = None, k = None,
                      h=None):
    '''
    Solve the linear dispersion relation. Need 2/3
        - (T,sigma)
        - (L,k)
        - h
    '''
    # Define gravity
    g = 9.81
    
    # Case 1: Given a period/frequency & water depth, find wavelength/wavenumber
    if ((T is None) != (sigma is None)) and L is None and k is None and h is not None:
        
        # Define sigma
        if sigma is None:
            sigma = 2 * np.pi / T
        
        # Definition of the linear dispersion relation
        def disp_relation(k):
            return sigma**2 - g * k * np.tanh(k * h)
        
        # Linear root finding
        k = brentq(disp_relation, 1e-12, 10)
        L = 2 * np.pi / k
        return k,L
    
    # Case 2: Given a wavelength/wavenumber & water depth, find period/frequency
    elif ((k is None) != (L is None)) and sigma is None and T is None and h is not None:
        # Define k
        if k is None:
            k = 2*np.pi/L
        
        # Calculate from linear dispersion
        sigma = np.sqrt(g*k*np.tanh(k*h))
        T = 2*np.pi/sigma
        
        return sigma,T
    
    # Case 3: Given a wavelength/wavenumber & period/frequency, find water depth
    elif ((k is None) != (L is None)) and ((T is None) != (sigma is None)) and h is None:
        # Define sigma
        if sigma is None:
            sigma = 2 * np.pi / T
            
        # Define k
        if k is None:
            k = 2*np.pi/L
            
        # Calculate from linear dispersion
        h = (1/k)*np.arctanh(sigma*sigma/(g*k))
        
        return h
            
            
def get_limits_where(H,L):
    T = []

    for h,l in zip(H,L) :
        sigma,T_ = linear_dispersion(L=l,h=h)
        T.append(T_)
        
    return np.array(T)
    
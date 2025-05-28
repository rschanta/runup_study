
from .dispersion import linear_dispersion



def get_hydrodynamics(var_dict):
    '''
    The purpose of this function is to get the wavelength from linear dispersion
    and deal with the whole regular vs. irregular thing
    '''
    # UNPACK ------------------------------------------------------------------
    T = var_dict['Tperiod']
    EPSILON = var_dict['EPSILON']
    h = var_dict['DEPTH_FLAT']
    # [END] UNPACK ------------------------------------------------------------

    # Get wavelength from linear dispersion
    k,L = linear_dispersion(T = T,h = h)
    
    AMP_WK = EPSILON/(2*h)
    
    # If wavemaker type is irregular, need Tperiod -> FreqPeak, AMP_WK -> Hmo
    FreqPeak = 1/T
    Hmo = 2*AMP_WK
    
    # Calculate kh
    kh = k*h
    # Calculate c
    c = L/T
    
    return {'k': k,
            'L': L,
            'kh': kh,
            'AMP_WK': AMP_WK,
            'c': c,
            'FreqPeak': FreqPeak,
            'Hmo': Hmo}
 

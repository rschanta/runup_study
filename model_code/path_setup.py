import os

def setup_path(var_dict):
    '''
    Sets up paths along the general guidelines from Marrissa Email

    wave type (regular/irregular) > slp > cd > relative wave height (relH).

    '''
    # UNPACK ------------------------------------------------------------------
    base = var_dict['base_path']
    WK = var_dict['WAVEMAKER']
    SLP = var_dict['SLP']
    CD = var_dict['Cd_Regional']
    EPS = var_dict['EPSILON']
    T = var_dict['Tperiod']
    h = var_dict['DEPTH_FLAT']
    # [END] UNPACK ------------------------------------------------------------
    
    # Make into nicer strings
    SLP_str = f"SLP{SLP:.3f}".replace('.', 'd')
    CD_str = f"CD{CD:.2f}".replace('.', 'd')
    EPS_str = f"EPS{EPS:.2f}".replace('.', 'd')
    T_str = f'T{int(T):02d}'
    h_str = f'h{int(h):02d}'
    
    # Directory for this
    dirs_make = os.path.join(base,WK,SLP_str,CD_str,EPS_str)
    # ID for this
    th_ID = T_str + h_str
    
    return {'trial_dirs': dirs_make,
            'th_ID': th_ID}
    
    
    
    
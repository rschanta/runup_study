import numpy as np

def filter_deep_water(var_dict):
    '''
    Removes any trials found to be in deep water
    '''
    # UNPACK ------------------------------------------------------------------
    kh = var_dict['kh']
    # [END] UNPACK ------------------------------------------------------------
    
    if kh < np.pi:
        return True
    else:
        return False
    
    
def filter_dx_70_cond(var_dict):
    '''
    Removes any trials found to be in deep water
    '''
    # UNPACK ------------------------------------------------------------------
    L = var_dict['L']
    h = var_dict['DEPTH_FLAT']
    # [END] UNPACK ------------------------------------------------------------
    
    if h/15 < L/70:
        return True
    else:
        return False
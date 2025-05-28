import numpy as np
def set_up_gages(var_dict):
    '''
    Here, the station position is first set in dimensional space, and then 
    converted to index space (i). All of these are concatenated together into
    a single matrix at the end as needed for gages.txt
    '''
    # UNPACK ------------------------------------------------------------------
    Xc_WK = var_dict['Xc_WK']
    Xslp = var_dict['Xslp']
    L = var_dict['L']
    DX = var_dict['DX']
    x_axis = var_dict['x_axis']
    i_slope = var_dict['i_slope']
    # [END] UNPACK ------------------------------------------------------------
    
    ## CONTROL STATIONS
    c_sta =np.array([Xc_WK + 1.333*L, (Xc_WK+Xslp)/2])
    c_sta_i = np.array(c_sta/DX + 1).astype(int)
    
    # REFLECTION STATIONS
    re_sta_frac = np.array([13/9,11/9,10/9,4/9,2/9,1/9])
    re_sta = []
    for frac in re_sta_frac:
        re_sta.append(Xslp-frac*L)
    # Convert to index space
    re_sta = np.array(re_sta)
    re_sta_i = np.array(re_sta/DX + 1).astype(int)
    
    # RUNUP STATIONS
    ru_sta = x_axis[i_slope:]
    ru_sta_i = np.array(ru_sta/DX + 1).astype(int)
    
    # ENTIRE FRICTION MATRIX
    gages_M = np.concatenate([c_sta_i, re_sta_i, ru_sta_i])
    gages_N = np.ones_like(gages_M)
    gage_file = np.column_stack([gages_M, gages_N])

    
    return {'reflection_pos': re_sta,
            'control_stations': c_sta,
            'gage_file': gage_file}
   

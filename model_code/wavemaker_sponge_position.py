import numpy as np
def set_wavemaker_sponge_pos(var_dict):
    # UNPACK ------------------------------------------------------------------
    # PI Parameters
    PI_1 = var_dict['PI_1']
    PI_2 = var_dict['PI_2']
    # Tau parameters
    TAU_1 = var_dict['TAU_1']
    # Geometry
    DEPTH_FLAT = var_dict['DEPTH_FLAT']
    # Hydrodynamics
    L = var_dict['L']
    c = var_dict['c']
    # Domain
    x = var_dict['x_axis']
    z = var_dict['z']
    # [END] UNPACK ------------------------------------------------------------
    
    # Set Xc_WK
    Xc_WK = (PI_1+PI_2)*L
    # DEP_WK
    DEP_WK = DEPTH_FLAT
    # Set sponge west width
    Sponge_west_width = (PI_1+PI_2)*L
    
    # Find distance from wavemaker to shoreline
    i_shore = np.argmin(np.abs(z))
    x_shore = x[i_shore]
    prop_distance = x_shore - Xc_WK

    # Calculate how much time it takes for the wave to propagate there
    prop_time = prop_distance/c
    # Set total time based on this
    TOTAL_TIME = TAU_1*prop_time
    
    
    
    return {'Sponge_west_width': Sponge_west_width,
            'Xc_WK': Xc_WK,
            'DEP_WK': DEP_WK,
            'TOTAL_TIME':TOTAL_TIME}
    
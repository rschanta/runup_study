import numpy as np





def set_up_friction(var_dict):
    # UNPACK ------------------------------------------------------------------
    i_slope = var_dict['i_slope']
    x_axis = var_dict['x_axis']
    Cd_regional = var_dict['Cd_Regional']
    # [END] UNPACK ------------------------------------------------------------
    
    friction_matrix = np.zeros_like(x_axis)
    friction_matrix[i_slope:] = Cd_regional
    
    return {'FRICTION_MATRIX': friction_matrix}
    


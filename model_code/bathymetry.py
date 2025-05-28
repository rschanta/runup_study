import numpy as np

def set_up_bathy(var_dict):
    # UNPACK ------------------------------------------------------------------
    # PI Parameters
    PI_1 = var_dict['PI_1']
    PI_2 = var_dict['PI_2']
    PI_3 = var_dict['PI_3']
    PI_4 = var_dict['PI_4']
    # Hydrodynamics
    L = var_dict['L']
    # Geometry
    DEPTH_FLAT = var_dict['DEPTH_FLAT']
    SLP = var_dict['SLP']
    # [END] UNPACK ------------------------------------------------------------
    
    
    # Set DX = lambda/70
    DX = L/70
    # Calculate what Mglob and Xslp must be from equations
    Mglob = int((L*(PI_1+PI_2 + PI_3+PI_4) + DEPTH_FLAT/SLP)/DX)
    Xslp = L*(PI_1 +PI_2+PI_3)
    
    ## CONSTRUCT X
    # Make the x-axis
    x_axis = DX*np.arange(0,Mglob)
    # Find where the slope begins in index space
    i_slope = int(Xslp/DX)+1
    # Split the x_axis into flat and slope regions
    x_flat,x_slope = x_axis[:i_slope],x_axis[i_slope:]
    
    ## CONSTRUCT Z
    # Make the flat region
    z_flat = DEPTH_FLAT*np.ones_like(x_flat)
    # Make the sloped region
    z_slope = -SLP*(x_slope-Xslp) + DEPTH_FLAT
    # Concatenate
    z = np.hstack([z_flat,z_slope])
    
    return {'DX': DX,
            'DY': DX,
            'Mglob': Mglob,
            'Xslp': Xslp,
            'x_axis': x_axis,
            'z': z,
            'i_slope': i_slope} 



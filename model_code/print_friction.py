import os
import numpy as np

def print_friction_file(var_dict):
    # UNPACK ------------------------------------------------------------------
    base_path = var_dict['trial_dirs']
    th_ID = var_dict['th_ID']
    FRICTION_MATRIX = var_dict['FRICTION_MATRIX']
    # [END] UNPACK ------------------------------------------------------------
    
    # Tile the bathymetry for Nglob = 3
    FRICTION_MATRIX_FILE = np.tile(FRICTION_MATRIX, (3, 1))  
    
    # Make directory if needed, file name, save out
    os.makedirs(base_path,exist_ok=True)
    FRICTION_FILE = os.path.join(base_path,f'friction_{th_ID}.txt')
    np.savetxt(FRICTION_FILE, FRICTION_MATRIX_FILE, fmt='%.6f') 
    return {'FRICTION_FILE': FRICTION_FILE}
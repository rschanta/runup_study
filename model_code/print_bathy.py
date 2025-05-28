import os
import numpy as np

def print_bathy(var_dict):
    # UNPACK ------------------------------------------------------------------
    base_path = var_dict['trial_dirs']
    th_ID = var_dict['th_ID']
    z = var_dict['z']
    
    # [END] UNPACK ------------------------------------------------------------
    
    # Tile the bathymetry for Nglob = 3
    DEP_FILE = np.tile(z, (3, 1))  
    
    # Save out
    os.makedirs(base_path,exist_ok=True)
    bathy_file = os.path.join(base_path,f'bathy_{th_ID}.txt')
    np.savetxt(bathy_file, DEP_FILE, fmt='%.6f') 
    return {'DEPTH_FILE': bathy_file}
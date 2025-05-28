import os
import numpy as np

def print_gage_file(var_dict):
    
    # UNPACK ------------------------------------------------------------------
    base_path = var_dict['trial_dirs']
    th_ID = var_dict['th_ID']
    gage_file = var_dict['gage_file'].astype(int)
    # [END] UNPACK ------------------------------------------------------------
    
    
    # Make directory if needed, file name, save out
    os.makedirs(base_path,exist_ok=True)
    gage_path = os.path.join(base_path,f'gages_{th_ID}.txt')
    np.savetxt(gage_path, gage_file, fmt='%d')
    return {'STATION_FILE': gage_path}
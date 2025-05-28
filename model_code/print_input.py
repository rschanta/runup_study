import copy
import os
def print_input_file(var_dict):
    # UNPACK ------------------------------------------------------------------
    base_path = var_dict['trial_dirs']
    #ITER = var_dict['ITER']
    th_ID = var_dict['th_ID']
    # [END] UNPACK ------------------------------------------------------------

    # Make directory if needed, file name, save out
    os.makedirs(base_path,exist_ok=True)
    input_path = os.path.join(base_path,f'input_{th_ID}.txt')

    var_dict_copy = copy.deepcopy(var_dict)
    with open(input_path, 'w') as f:
        for var_name, value in var_dict_copy.items():
            if isinstance(value, (str, int, float)):
                f.write(f"{var_name} = {value}\n")
    
    print(f"\tinput.txt file successfully saved to: {input_path}")
    return {}
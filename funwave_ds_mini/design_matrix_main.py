from .combinations_from_dict import find_combinations_from_dict
from .filtering import apply_filters
from .add_params import add_dependent_values,add_print_functions,add_required_params

import numpy as np
import pandas as pd

def process_design_matrix(matrix_dict=None,
                            function_set = None, 
                            filter_sets = None,
                            print_sets = None, 
                            plot_sets = None,
                            summary_formats = ['parquet','csv']):
    ## Initialization
    fail_data,pass_data = [],[] 
    k = 1                       
    
    ## Load in design matrix, parse variables, and group
    df_permutations = find_combinations_from_dict(matrix_dict)
    print(f'{len(df_permutations)} DIFFERENT COMBINATIONS POSSIBLE')
    
    #------------------------ Beginning of Loop-----------------------------#   
    for perm_i, row in df_permutations.iterrows():
        print(f'\nStarted processing permutation: {perm_i:05}...',flush=True)
        # Keep track of the combination index, regardless if it fails
        combo_num = perm_i + 1
    
        # Convert row to dictionary form
        var_dict = row.to_dict()
        
        ## Add on dependent parameters
        var_dict = add_dependent_values(var_dict,function_set)
        
        ## Filtering conditions
        failed_params = apply_filters(var_dict,filter_sets)      
        
        # Failure Cases:
        if failed_params is not None:
            # Add on required parameters (just combo num)
            failed_params['COMBO_NUM'] = combo_num
            # Append to list
            failed_params = {k: v for k, v in failed_params.items() if not isinstance(v, np.ndarray)}
            fail_data.append(failed_params)
            print(f'Combination {combo_num:05} FAILED. Moving on.')
    
        ## No failures: proceed to output
        elif failed_params is None:    
            ##  Add on required parameters
            var_dict = add_required_params(var_dict,k,combo_num)
            
            # APPLY PRINT FUNCTIONS
            var_dict = add_print_functions(var_dict,print_sets)
            
            
            ## Remove numpy arrays for compression into dataframe
            var_dict = {k: v for k, v in var_dict.items() if not isinstance(v, np.ndarray)}
            pass_data.append(var_dict)
    
            ## End loop iteration
            print(f'SUCCESSFULLY PRINTED FILES FOR TRIAL: {k:05}',flush=True)
            print('#'*40)
            k = k + 1
       
    df_fail = pd.DataFrame(fail_data)
    df_pass = pd.DataFrame(pass_data)
    
    return df_fail, df_pass
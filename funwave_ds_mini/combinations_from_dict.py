import pandas as pd
import numpy as np
from itertools import product

from .assertion import assert_design_matrix_dict
from .convert_to_number import convert_to_number


def find_combinations_from_dict(input_dict):
    # 
    print('\nRANGES OF FUNWAVE-TVD VALUES' + '=' * (80 - len('\nRANGES OF FUNWAVE-TVD VALUES')))
    # Assert condition
    assert_design_matrix_dict(input_dict)
    # Loop through each category
    
    param_ranges = {}
    for category, category_dict in input_dict.items():
        print(f'{category}' + '-' * (80 - len(category)))
        
        
        # Loop through each FUNWAVE parameter
        for FW_PARAM_NAME, FW_PARAM_VALUES in category_dict.items():
            val_list = []
            print(f'\t{FW_PARAM_NAME}')
            
            # If value is just a string, add to list
            if isinstance(FW_PARAM_VALUES, str):
                # Convert and append to list
                value =  convert_to_number(FW_PARAM_VALUES)
                val_list.append(value)
                print(f'\t\t• CONSTANT: {FW_PARAM_VALUES}')
                
            # If a tuple, it's a ranged parameter
            elif isinstance(FW_PARAM_VALUES, tuple):
                print(f"\t\t• RANGED: np.linspace({FW_PARAM_VALUES[0]},{FW_PARAM_VALUES[1]},{FW_PARAM_VALUES[2]})")
                val_list.extend(np.linspace(FW_PARAM_VALUES[0],FW_PARAM_VALUES[1],FW_PARAM_VALUES[2]))
            
            # If value is a list, it's either a list/ranged parameter
            elif isinstance(FW_PARAM_VALUES, list):
                for entry in FW_PARAM_VALUES:
                    # Deal with constants
                    if isinstance(entry,str):
                        value =  convert_to_number(entry)
                        val_list.append(value)
                        print(f'\t\t• CONSTANT: {value}')
                        
                    # Deal with ranges
                    if isinstance(entry,tuple):
                        print(f"\t\t• RANGED: np.linspace({entry[0]},{entry[1]},{entry[2]})")
                        val_list.extend(np.linspace(entry[0],entry[1],entry[2]))
                        
            # Add onto ranges
            param_ranges[FW_PARAM_NAME] = val_list
    
    # Find all combinations and convert to dataframe
    combinations = list(product(*param_ranges.values()))
    dfv = pd.DataFrame(combinations, columns=param_ranges.keys())
    
    print('='*80)
    return dfv

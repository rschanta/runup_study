def add_dependent_values(var_dict,
                         functions_to_apply):
    '''
    Add on dependency parameters defined by a pipeline. This is applied to
    each ROW of the design matrix

    Arguments:
    - var_dict (dictionary): dictionary of FUNWAVE parameters
    - functions_to_apply (list): list of functions defining the pipeline

    Returns:
    - var_dict (dictionary): dictionary of FUNWAVE parameters, with dependent
        parameters added on
    '''
    print('\nApplying DEPENDENCY functions')
    
    
    # Loop through to apply each dependency function
    dependent_vars = {}
    for func in functions_to_apply:
        print(f'\tApplying DEPENDENCY function: {func.__name__}')

        # Calculate
        result = func(var_dict)
        # Update
        dependent_vars.update(result)
        # Merge
        var_dict = {**var_dict, **dependent_vars}

    print('All DEPENDENCY functions completed successfully!')
    return var_dict


    
def add_required_params(var_dict,iter_num,comb_i):
    '''
    Add in parameters that FUNWAVE either needs or that we need to keep track
    of everything. This is applied to each ROW of the design matrix
    '''
    
    # Title of Run- use iteration number to keep things tidy
    var_dict['TITLE'] = f'input_{iter_num:05}'
    # Result Folder
    var_dict['RESULT_FOLDER'] = var_dict['rf_path']    
    # ITERATION NUMBER  
    var_dict['ITER'] = iter_num   
    # COMBINATION NUMBER
    var_dict['COMBO_NUM'] = comb_i                                  
    
    return var_dict


def add_print_functions(var_dict,
                         functions_to_apply):
    '''

    '''
    print('\nApplying PRINT functions')
    
    
    # Loop through to apply each dependency function
    dependent_vars = {}
    for func in functions_to_apply:
        print(f'\tApplying PRINT function: {func.__name__}')

        # Calculate
        result = func(var_dict)
        # Update
        dependent_vars.update(result)
        # Merge
        var_dict = {**var_dict, **dependent_vars}

    print('All PRINT functions completed successfully!')
    return var_dict
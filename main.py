import model_code as mod
import funwave_ds_mini as fds
import matplotlib.pyplot as plt
import sys

'''
This will print a bunch of stuff to an output log. comment it out just to do 
it in console.
'''
sys.stdout = open('output.log', 'w')

#%% INITIALIZE THE DESIGN MATRIX
'''
This just outputs a dictionary for all of the basic variables that will be 
set common in the run. Edit the function itself if necessary
'''
var_dict = mod.design_matrix_base()


'''
Here, we add on the nondimensionalize parameters that specify the problem 
geometry in terms of representative wavelengths, amplidues, periods, etc.

    - PI_1: width of sponge
    - PI_2: distance from sponge to Xc_WK
    - PI_3: distance from Xc_WK to Xslp
    - PI_4: distance of the dry beach (allows room for runup)
    - TAU_1: time measure for how long it takes for the wave to propagate to 
        the shoreline. 
    - EPSILON: relative wave height H/h. Works for either WK_REG or WK_IRR
'''
var_dict['NONDIM'] = {'PI_1': "2.0",
                      'PI_2': "1.0",
                      'PI_3': "4.0",
                      'PI_4': "1.0",
                      'TAU_1': "4.0",
                      'EPSILON': ['0.1', '0.25', '0.5']}

'''
Here, we add on the main suite of variables we're looking to vary in this study

    - Tperiod: note that this will work for either WK_REG or WK_IRR. In the 
        case of WK_IRR, it's converted to `FreqPeak` just be taking 1/Tperiod.
        See the `model_code/hydrodynamics.py` script     
    - DEPTH_FLAT: offshore depth
    - Cd_Regional: the strength of friction applied solely for the sloping 
        region. A corresponding FRICTION_MATRIX file will be generated with
        this as a constant just along the slope.
    - SLP: The slope as it would be used in the DEPTH_TYPE=SLP type bathymetry.
        I wasn't sure if you could actually use this DEPTH_TYPE with a 
        FRICTION_MATRIX, so technically I use a DEPTH_TYPE=DATA and just 
        construct the equivalent bathymetry manually and output it as a 
        DEPTH_FILE
    
''' 
var_dict['VARIABLES'] = {'TAU_1': "4.0",
                      "Tperiod": (2,16,15),
                      'Cd_Regional': "1.0",
                      "DEPTH_FLAT": (1,20,20),
                      "WAVEMAKER": ['WK_IRR','WK_REG'],
                      "SLP": ['0.5', '0.333', '0.2', '0.125']}

'''
This is where all of the files will be generated. If they don't exist, they'll
be created, except for `rf_path`. Note that these will also impact the 
input.txt file for every run so they can all point to the correct path. 

    - rf_path: the base path used for the RESULT_FOLDER of each trial. Note 
        that this is just the base. A unique number gets added to each one
        as an ID of sorts
    - base_path: path locally to throw all the outputs
'''
var_dict['PATHS']   = {
                      'rf_path': 'test',
                      'base_path': './out'}


#%% PIPELINE
'''
These functions are applied one after another, effectively chaining together
operations to pass along information and create variables
    - get_hydrodynamics: calculate wavelength, velocity, all that stuff
    - set_up_bathy: use the pi parameters and DEPTH_TYPE=SLP geometry to figure
        out all the relevant bathymetry parameters
    - set_wavemaker_sponge_pos: set the wavemaker and sponge position, as well
        as TOTAL_TIME
    - set_up_friction: creates the friction matrix along the slope
    - set_up_gages: figures out where to place the gages
    - setup_path: setups all the needed paths
'''
function_set = [mod.get_hydrodynamics,
                 mod.set_up_bathy,
                 mod.set_wavemaker_sponge_pos,
                 mod.set_up_friction,
                 mod.set_up_gages,
                 mod.setup_path]
#%% FILTERING
'''
These functions just return a boolean as to whether or not this combination of 
variables should be used or not. Add or remove as you see fit.
    - filter_deep_water: returns False for kh > pi
    - filter_dx_70_cond: returns False for h/15 > L/70
'''
filter_sets = [mod.filter_deep_water,
               mod.filter_dx_70_cond]

#%% PRINT
'''
These functions specify how the actual files get printed out
    - print_bathy: DEPTH_FILE
    - print_gage_file: station file
    - make_domain_figure: a little plot of the domain
    - print_input_file: input.txt file
'''

outputs = [mod.print_bathy,
           mod.print_gage_file,
           mod.make_domain_figure,
           mod.print_friction_file,
           mod.print_input_file]

#%% MAIN
'''
Applies everything, returning dataframes for the ones that failed and the ones
that were successful.
'''


df_fail, df_pass = fds.process_design_matrix(matrix_dict=var_dict,
                                            function_set = function_set, 
                                            filter_sets = filter_sets,
                                            print_sets = outputs)

# Save variables to parquet
df_pass.to_parquet('runup_study.parquet')
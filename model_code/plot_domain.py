import matplotlib.pyplot as plt
import numpy as np
import os

def make_domain_figure(var_dict):
    # UNPACK ------------------------------------------------------------------
    # Geometry
    DEPTH_FLAT = var_dict['DEPTH_FLAT']
    SLP = var_dict['SLP']
    # Friction
    Cd_Regional = var_dict['Cd_Regional']
    # Period
    T = var_dict['Tperiod']
    EPSILON = var_dict['EPSILON']
    # Calculated
    DX = var_dict['DX']
    Mglob = var_dict['Mglob']
    Xslp = var_dict['Xslp']
    L = var_dict['L']
    Xc_WK = var_dict['Xc_WK']
    SLP = var_dict['SLP']
    SWW = var_dict['Sponge_west_width']
    friction_matrix = var_dict['FRICTION_MATRIX']
    reflection_pos = var_dict['reflection_pos']
    control_stations = var_dict['control_stations']
    ITER = var_dict['ITER']
    # Domain fig
    trial_dirs = var_dict['trial_dirs']
    th_id = var_dict['th_ID']
    # [END] UNPACK ------------------------------------------------------------
    
    
    ## CONSTRUCT BATHYMETRY ---------------------------------------------------
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
    ## [END] CONSTRUCT BATHYMETRY ---------------------------------------------
    
    
    fig,ax = plt.subplots(dpi=200)
    
    ## FIND SHORELINE 
    i_shore = np.argmin(np.abs(z))
    x_wet = x_axis[:i_shore+1]
    z_wet = np.zeros_like(x_wet)
    
    ## BASIC PLOT ELEMENTS ----------------------------------------------------
    # Bathymetry
    ax.plot(x_axis,-z,color='black')
    # MWL
    ax.plot(x_wet,z_wet,color='blue')
    # Sponge layer
    ax.fill_between([0,SWW],[-DEPTH_FLAT,-DEPTH_FLAT],[0,0],
                    alpha=0.5,color='green',label='Sponge')
    # Wavemaker
    ax.axvline(Xc_WK,ls='--',color='red',label='Xc_WK')
    # Wet non-sponge area
    i_WK = np.argmin(np.abs(Xc_WK-x_axis))
    x_dom = x_axis[i_WK:i_shore+1]
    z_dom = z[i_WK:i_shore+1]
    ax.fill_between(x_dom,-z_dom,np.zeros_like(z_dom),color='lightblue',alpha=0.25)
    ## [END] BASIC PLOT ELEMENTS ----------------------------------------------
    
    # FRICTION ----------------------------------------------------------------
    # Manually check that this is what we think it is
    nz = np.flatnonzero(friction_matrix)
    ax.plot(x_axis[nz[0]:nz[-1]+1],-z[nz[0]:nz[-1]+1],
            color='purple',label='Friction Region\nGage every DX')
    # [END] FRICTION ----------------------------------------------------------
    
    
    ## GAGES ------------------------------------------------------------------
    # Plot the reflection gages
    for i,pos in enumerate(reflection_pos):
        if i == 0:
            ax.axvline(pos,label='Reflection Gages',ls='-.',color='grey')
        else:
            ax.axvline(pos,ls='-.',color='grey')
            
    # Plot the control gages
    for i,pos in enumerate(control_stations):
        if i == 0:
            ax.axvline(pos,label='Control Gages',ls='-',color='brown')
        else:
            ax.axvline(pos,ls='-',color='brown')
    ## [END] GAGES ------------------------------------------------------------      
    
    
    ## FORMATTING -------------------------------------------------------------
    ax.set_xlim(0,np.max(x_axis))
    ax.set_ylim(-1.05*DEPTH_FLAT,-np.min(z))
    ax.legend(bbox_to_anchor=(0.5,-0.25),loc='upper center',ncol=3)
    ax.set_title(f'Trial {ITER}, T = {T} s, h = {DEPTH_FLAT} m' +
                 f'\nSLP={SLP},$C_D$ ={Cd_Regional} $\\epsilon$ = {EPSILON}')
    fig.tight_layout()
    ## [END] FORMATTING -------------------------------------------------------
    
    
    ## SAVE OUT
    # Make directory if needed, file name, save out
    os.makedirs(trial_dirs,exist_ok=True)
    domain_file = os.path.join(trial_dirs,f'domain_{th_id}.png')
    fig.savefig(domain_file)
    plt.close(fig)
    return {}


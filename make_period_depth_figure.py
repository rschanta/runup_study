import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%% Load in variables that passed
df_pass = pd.read_parquet('runup_study.parquet')


#%% Basic Figure
fig,ax = plt.subplots(dpi=200)
ax.scatter(df_pass['Tperiod'],df_pass['DEPTH_FLAT'],
           marker='s',s=15,color='black')
ax.set_xlabel('Period'); ax.set_ylabel('Depth')
ax.set_xlim(0.75,17)
ax.set_ylim(0.5,21)


#%% Add on contours and shaded regions of interest
def get_limit_T_axis(factor,h):
    '''
    This finds the curves in the T-h plane for the given condition of interest,
    returning the corresponding T values for h. factor = 70/15 is the 
    curve defining the boundary where h/15 = L/70, for example, so 
    L = (70/15)h.
    '''
    L = factor*h
    sigma = np.sqrt(9.81*(2*np.pi/L)*np.tanh((2*np.pi/L)*h))
    T = 2*np.pi/sigma
    return T


## Periods and depths to use on the plot
T_lo, T_hi= 0, 17
h_vals = np.linspace(0, 21, 500)

# Get the limits, construct out to end
T_val_deep = get_limit_T_axis(2,h_vals)
T_val_70 = get_limit_T_axis(70/15,h_vals)
T_val_60 = get_limit_T_axis(60/15,h_vals)
T_val_shallow = get_limit_T_axis(20,h_vals)



# Deep Water Limit 
ax.plot(T_val_deep,h_vals,lw=3,color='red')
# L/60 = h/15 line
ax.plot(T_val_60,h_vals,lw=3,color='orange')
# L/70 = h/15 line
ax.plot(T_val_70,h_vals,lw=3,color='purple')
# Shallow Water Limit 
ax.plot(T_val_shallow,h_vals,lw=3,color='brown')


# Deep Water Region
ax.fill_betweenx(h_vals, 
                 T_lo, 
                 T_val_deep, 
                 color='red', alpha=0.3, label='$kh>\\pi$')

# Region between deep water and L/60 = h/15 line
ax.fill_betweenx(h_vals, 
                 T_val_deep, 
                 T_val_60, 
                 where=T_val_deep < T_val_60, 
                 color='orange', alpha=0.3, label='$\\frac{\lambda}{60}<\\frac{h}{15}$')
# Region between L/70 = h/15 and L/60 = h/15 line
ax.fill_betweenx(h_vals, 
                 T_val_70, 
                 T_val_60, 
                 where=T_val_60 < T_val_70, 
                 color='purple', alpha=0.3, label='$\\frac{\lambda}{70}<\\frac{h}{15}$')

# Intermediate
ax.fill_betweenx(h_vals, 
                 T_val_70, 
                 T_val_shallow, 
                 where=T_val_70 < T_val_shallow, 
                 color='grey', alpha=0.3)

# Shallow
ax.fill_betweenx(h_vals, 
                 T_val_shallow, 
                 T_hi, 
                 where=T_val_shallow < T_hi, 
                 color='brown', alpha=0.3, label='$kh<\\pi/10$')

ax.legend(bbox_to_anchor=(0.5,-0.2),loc='upper center',ncol=4)
ax.set_title(f'Runup Study n={len(df_pass)}')
fig.tight_layout()






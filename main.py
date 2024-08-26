#%% Import of external packages (*distibution*/../ -> python environment)
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#%% Import of internal packages (./ -> working directory)
# Import and init. of "corporate" colors
import mod.kitc as kit; kit.init()
# Import of custom plot style framework
import mod.prpm as plot_style 

# Script layer -> initialization of selected matplotlib parameters
plot_style.init(delete_cache=False, save_fig=False, name='no_name',
                font_size=12, font_family='sans-serif', font='Arial',
                canvas_columns=1, canvas_width_cm=16, aratio=[1, 1])

#%% Example #1 - Plot fitting whole width of document
# Individual plot layer -> (Re-)initialization of mpl parammeters
plot_style.init(delete_cache=False, save_fig=True, name='example_plot_1', 
                font_size=12, font_family='serif', font='Latin Modern Roman',
                canvas_columns=1, canvas_width_cm=15.99, aratio=[2, 1])

fig, ax = plt.subplots(constrained_layout=True)

# Data
## Line-Plot based on 4 point coordinate tuples [x,y]
ax.plot([0.1,0.2,0.3,0.4], # x-data
        ([0.1,0.2,0.3,0.4]), # y-data
        color='black', linewidth=1, linestyle='--', # line options
        zorder=0, # draw layer
        label='Line' # name of data (for legend referencing)
        )

## Scatter-Plot based on 1 coordinate tuple [x,y]
ax.scatter([0.1,0.2,0.3,0.4], # x-data
            ([0.1,0.2,0.3,0.4]), # y-data
            color='green', linewidth=1, 
            edgecolors='black', marker='o', # marker options
            zorder=1, # draw layer
            label='Scatter' # name of data (for legend referencing)
            )

# ---- Options: Axes & Layout
# --- Labels
ax.set_xlabel('Publication ready label $x$ /-') # define the axis label
ax.set_ylabel('Publication ready label $y$ /-')
# --- Scale
ax.set_xscale('linear') # choose between 'linear' and 'log'
ax.set_yscale('linear') # choose between 'linear' and 'log'
# --- Limits
ax.set_xlim(left=0,right=0.5)
ax.set_ylim(bottom=None,top=0.5)
# --- Legend
ax.legend(loc='lower left', fontsize='small', framealpha=1, ncol=1)
# --- Layout
layout_type = 'constrained' # 't' # 'h'

if layout_type == 't':
    plt.tight_layout()
    
elif layout_type == 'h':
    plt.subplots_adjust(
        top=0.994,
        bottom=0.227,
        left=0.152,
        right=0.845,
        hspace=0.2,
        wspace=0.2)
    
# ---- Optional: Plot export
if plot_style.execute_save == True:
    fig.savefig('export/'+f'{plot_style.set_name}'+ '.pdf')
    
#%% Example #2 - Plot fitting half width of document
# Individual plot layer -> (Re-)initialization of mpl parammeters
plot_style.init(delete_cache=False, save_fig=False, name='example_plot_2',  
                font_size=12, font_family='serif', font='Latin Modern Roman',
                canvas_columns=2, canvas_width_cm=15.99, aratio=[1.1, 1])

fig, ax = plt.subplots(constrained_layout=True)

# Data
## Line-Plot based on 4 point coordinate tuples [x,y]
ax.plot([0.1,0.2,0.3,0.4], # x-data
        ([0.1,0.2,0.3,0.4]), # y-data
        color='black', linewidth=1, linestyle='--', # line options
        zorder=0, # draw layer
        label='Line' # name of data (for legend referencing)
        )

## Scatter-Plot based on 1 coordinate tuple [x,y]
ax.scatter([0.1,0.2,0.3,0.4], # x-data
            ([0.1,0.2,0.3,0.4]), # y-data
            color='green', linewidth=1, 
            edgecolors='black', marker='o', # marker options
            zorder=1, # draw layer
            label='Scatter' # name of data (for legend referencing)
            )

# ---- Options: Axes & Layout
# --- Labels
ax.set_xlabel('Publication ready label $x$ /-') # define the axis label
ax.set_ylabel('Publication ready label $y$ /-')
# --- Scale
ax.set_xscale('linear') # choose between 'linear' and 'log'
ax.set_yscale('linear') # choose between 'linear' and 'log'
# --- Limits
ax.set_xlim(left=0,right=0.5)
ax.set_ylim(bottom=None,top=0.5)
# --- Legend
ax.legend(loc='upper left', fontsize='small', framealpha=1, ncol=1)
# --- Layout
layout_type = 'constrained' # 't' # 'h'

if layout_type == 't':
    plt.tight_layout()
    
elif layout_type == 'h':
    plt.subplots_adjust(
        top=0.994,
        bottom=0.227,
        left=0.152,
        right=0.845,
        hspace=0.2,
        wspace=0.2)
    
# ---- Options: Plot export
if plot_style.execute_save == True:
    fig.savefig('export/'+f'{plot_style.set_name}'+ '.pdf')
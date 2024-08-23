import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def init(delete_cache=False, 
         font_size=12, font_family='sans-serif', font='default', 
         canvas_columns=1, canvas_width_cm=16, aratio=[6.4, 4.8],
         dpi=96):
    #---- Reset rcParams to default
    plt.rcdefaults() 
    #%% FONTS  
    #%%% -> Family
    plt.rcParams['mathtext.fontset'] = 'cm'
    if font_family == 'serif':
        plt.rcParams['font.family'] = 'serif'
        if font == 'default':
            plt.rcParams['font.serif'] = ['DejaVu Serif', 'Times New Roman']
        else:
            plt.rcParams['font.serif'] = font
            
    elif font_family == 'sans-serif':
        plt.rcParams['font.family'] = 'sans-serif'
        if font == 'default':
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
        else:
            plt.rcParams['font.sans-serif'] = font
    else:
        raise ValueError('Invalid font family. Valid: serif | sans-serif')
    
    #%%% -> Size
    plt.rcParams['font.size'] = font_size # relative fontsize in unit "pt"
    ## relative sizes:
    ## xx-small, x-small, small, medium, large, x-large, xx-large, larger
    plt.rcParams['axes.titlesize'] = 'medium'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['legend.fontsize'] = 'medium'
    plt.rcParams['xtick.labelsize'] = 'small'
    plt.rcParams['ytick.labelsize'] = 'small'
    
    #%% FIGURE
    #%%% -> Size (scale is set automatically)
    fac_fp = canvas_width_cm/(2.54*aratio[0])
    fac_hp = canvas_width_cm/(2.54*aratio[0]*2)
    fac_tp = canvas_width_cm/(2.54*aratio[0]*3)
    if canvas_columns == 1:
        plt.rcParams['figure.figsize'] = [aratio[0]*fac_fp,aratio[1]*fac_fp]
    elif canvas_columns == 2:
        plt.rcParams['figure.figsize'] = [aratio[0]*fac_hp,aratio[1]*fac_hp]
    elif canvas_columns == 3:
        plt.rcParams['figure.figsize'] = [aratio[0]*fac_tp,aratio[1]*fac_tp]
    else:
        raise ValueError('Only column count of {1,2,3} supported')
        
    #%%% -> Color
    plt.rcParams['figure.facecolor'] = (1.0,1.0,1.0,0.0) # rgba
    plt.rcParams['figure.edgecolor'] = (1.0,1.0,1.0,0.0) # rgba
    
    #%%% -> Subfigure ALIGNMENT of axes in fig canvas
    plt.rcParams['figure.subplot.left'] = 0.1
    plt.rcParams['figure.subplot.right'] = 0.98
    plt.rcParams['figure.subplot.bottom'] = 0.1
    plt.rcParams['figure.subplot.top'] = 0.88
    plt.rcParams['figure.subplot.wspace'] = 0.2
    plt.rcParams['figure.subplot.hspace'] = 0.2
    
    #%%% -> Quality (size on display)
    plt.rcParams['figure.dpi'] = dpi
    
    #%% AXES
    plt.rcParams['axes.axisbelow'] = True
    #%%% -> Color
    plt.rcParams['axes.facecolor'] = (1.0, 1.0, 1.0, 0.0)
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.labelcolor'] = 'black'
    
    #%%% -> Lines
    plt.rcParams['axes.linewidth'] = 0.5
    
    #%%% -> Labels
    plt.rcParams['axes.labelpad'] = 2 # space between label and axis
    plt.rcParams['axes.labelsize'] = 'medium'
    
    #%% TICKS
    #%%% -> Display
    plt.rcParams['xtick.top'] = False
    plt.rcParams['xtick.bottom'] = True
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.left'] = True
    plt.rcParams['ytick.right'] = False
    plt.rcParams['ytick.minor.visible'] = True
    
    #%%% -> Lines
    plt.rcParams['xtick.major.size'] = 3
    plt.rcParams['xtick.major.width'] = plt.rcParams['axes.linewidth']
    plt.rcParams['xtick.minor.size'] = 1
    plt.rcParams['xtick.minor.width'] = plt.rcParams['axes.linewidth']/2
    plt.rcParams['ytick.major.size'] = 3
    plt.rcParams['ytick.major.width'] = plt.rcParams['axes.linewidth']
    plt.rcParams['ytick.minor.size'] = 1
    plt.rcParams['ytick.minor.width'] = plt.rcParams['axes.linewidth']/2
    
    #%%% -> Color
    plt.rcParams['xtick.color'] = 'black'
    plt.rcParams['ytick.color'] = 'black'
    
    #%% GRID
    #%%% -> Enable/Disable
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.grid.axis'] = 'both' #{'both','major','minor'}
    plt.rcParams['axes.grid.which'] = 'both' #{'both','major','minor'}
    
    #%%% -> Color
    plt.rcParams['grid.color'] = 'lightgray'
    
    #%%% -> Lines
    plt.rcParams['grid.linestyle'] = '-' # {'-','--',':','-.'}
    plt.rcParams['grid.linewidth'] = plt.rcParams['axes.linewidth']/2
    plt.rcParams['grid.alpha'] = 1
    
    #%% LEGEND
    #%%% -> Spacing
    plt.rcParams['legend.loc'] = 'upper left' 
    plt.rcParams['legend.columnspacing'] = 1 # horizontal legend entry spacing
    plt.rcParams['legend.labelspacing'] = 0.5  # vertical legend entry spacing
    plt.rcParams['legend.handletextpad'] = 0.4 # horizontal handle <-> text spacing
    plt.rcParams['legend.markerscale'] = 1
    plt.rcParams['legend.handlelength'] = 1
    plt.rcParams['legend.handleheight'] = 1
    plt.rcParams['legend.fontsize'] = 'medium'
    
    #%%% -> Color & Box
    plt.rcParams['legend.fancybox'] = True
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['legend.edgecolor'] = 'black'
    plt.rcParams['legend.framealpha'] = 1
    
    #%% Other
    if delete_cache == True: 
        plt.close('all')
    else: pass
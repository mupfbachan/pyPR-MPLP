import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def init(delete_cache=False, save_fig=False, name='no_name',
         font_size=12, font_family='sans-serif', font='default', 
         canvas_columns=1, canvas_width_cm=16, aratio=[6.4, 4.8],
         dpi=96):
    '''
    Parameters
        ----------
        delete_cache : bool
            Specify if previous plots in a script are deleted or not
        save_fig : bool
            Specify plot save execution argument for figure export
        name : string
            Specification of a plot name (export name allocation)
        font_size : int
            Sets the *medium* font size of the plot.
            Matplotlib uses relative expressions: 
                xx-small, x-small, small, medium, large, x-large, xx-large, larger
            Example font size specifications (can be adjusted by user in `prpm.py`:
                plt.rcParams['axes.titlesize'] = 'medium'
                plt.rcParams['axes.labelsize'] = 'medium'
                plt.rcParams['legend.fontsize'] = 'medium'
                plt.rcParams['xtick.labelsize'] = 'small'
                plt.rcParams['ytick.labelsize'] = 'small'
        font_family : string
            Sets mathtext.fontset to 'cm' (Computer Modern)
            User input can specify if font type is 'sans-serif' or 'serif'
        font : string
            Uses either 'default' fonts for chosen font family (needs to be installed on current os and accessible via the python terminal) or a user specified font given by the correct name.
        canvas_columns : int [1,2,3]
            Sets the figure size of the plot so that the specified number fit into the canvas width defined by 'canvas_width_cm'.
        canvas_width_cm : float
            Available canvas width (e.g. text width) in document (Unit: cm)
        aratio : tuple or list of int
            Defines the desired aspect ratio of the plot width:height
                (e.g. golden ratio: [1.62, 1])
        dpi : int
            Sets figure dpi (quality, size on display)

        Returns
        -------
        execute_save : bool
            GLOBAL parameter (accessible by **.execute_save)
        set_name : bool
            GLOBAL parameter (accessible by **.set_name)
    '''
    #---- Reset rcParams to default
    plt.rcdefaults()
    
    #---- Set global parameters
    global execute_save, set_name
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

    if save_fig == True: 
        execute_save = True
        set_name = name
    else: pass
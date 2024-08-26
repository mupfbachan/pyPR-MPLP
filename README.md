# Publication Ready Plots Matplotlib

A Python module for adjusting matplotlib parameters to display scientific data in a streamlined, clear and efficient form for publication

## Module description and features

This module can be implemented into any given workflow when dealing with python scripts performing operations on e.g. scientific research data or with data saved in any form of accessible database.

Key *matplotlib* runtime parameters are adjusted based on user inputs that are important for plot post-processing and embedding into documents. These parameters include:

* Font type and size
* Aspect ratio
* Color schemes
* Plot layout

## How to use this module

Copy the python module `prpm.py` in any active working directory to deploy all plot style adjustments features. For demonstration purposes, this repository created the directory `/mod` to organize modules where the main module code is located ( `/mod/prpm.py` ). Here, an accompanying module to import a *corporate design color palette* of the *Karlsruher Institute of Technology* ( `/mod/cdcp_kit.py `) is used, containing easy to access color definitions.

### Import modules

In your code, import all needed modules as usual:

```python
import mod.prpm as plot_style
import mod.kitc as kit
```

### Initialize modules

Both modules include an initialization function `*module_name*.init(...)`. For the corporate color module, the initialization simply enables the user to call any given color by name with e.g. the expression `kit.green` for a green color. In case of the `prpm` module, the initialization process sets both fixed and dynamic matplotlib parameters and style options. Some of them are initialized directly by the user when calling the `.init(*args,*kwargs)` function.

Important information is given in the `.init()` function docstring:

```python
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
```

### Important note on *matplotlib* syntax integration

The `prpm.py` module simply initializes some key runtime parameters and user-defined quirks for the final plot, aiming for a more streamlined deployment in documents. It does NOT interfere with the general *matplotlib* plot type and coding preferences of the user.

In other words: The user initializes the runtime parameter changes with `plot_style.init(..)` prior to data illustration and writes his own plot illustration code with the ***matplotlib* syntax**.

Basic example of this idea written in python:

```python
# ##############################################
# !!!!! Beginning of python scrip
# ##############################################
import mod.prpm as plot_style 
# ...

# ##############################################
# !!!!! e.g. data import, calculations ...
# ##############################################
# ...

# ##############################################
# !!!!! wish to illustrate data with matplotlib
# ##############################################
plot_style.init(delete_cache=False, save_fig=True, name='results_plot_1', 
                font_size=12, font_family='serif', font='Latin Modern Roman',
                canvas_columns=1, canvas_width_cm=15.99, aratio=[2, 1])

# ##############################################
# !!!!! MATPLOTLIB SYNTAX <- written by user
# ##############################################

# ---- Optional: Plot export
if plot_style.execute_save == True:
    fig.savefig('export/'+f'{plot_style.set_name}'+ '.pdf')

# ##############################################
# !!!!! End or Continuation of python script
# ##############################################
```
## Example python code

An example code is provided in the `main.py` script in this repository. 
Code tested with ...
... *miniconda* distribution environment
... *python version* `3.10.14`
... *matplotlib version* `3.8.4`
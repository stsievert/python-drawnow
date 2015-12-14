from __future__ import print_function
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import pdb

def drawnow(draw_fig, show_once=False, confirm=False, *argv, **kwargs):
    """A function to refresh the current figure.

    Depends on matplotlib's interactive mode. Similar functionality to MATLAB's
    drawnow.

    Parameters
    ----------
    draw_fig : callable
               the function that draws the figure you want to update
    *argv    : any
               the list of parameters to pass ``draw_fig()``
    **kwargs : any
               the keywords to pass to ``draw_fig()``
    show_once, optional : bool, default == False.
               If True, will call show() instead of draw().
    confirm, optional : bool, default == False
               If True, wait for user input after each iteration and present
               option to drop to python debugger (pdb).

    Limitations
    -----------
    - Occaisonally ignores Ctrl-C especially while processing LaTeX.
    - Does not work in IPython's QtConsole. This depends on pylab's
      interactivity (implemented via ion()) working in QtConsole.
    - The initial processing of Latex labels (typically on the x/y axis and
      title) is slow. However, matplotlib caches the results so any subsequent
      animations are pretty fast.
    - If two figures open and focus moved between figures, then other figure
      gets cleared.

    Usage Example
    -------------
      >>> from pylab import * # import matplotlib before drawnow
      >>> from drawnow import drawnow, figure
      >>> def draw_fig_real():
      >>>     #figure() # don't call, otherwise opens new window
      >>>     imshow(z, interpolation='nearest')
      >>>     colorbar()
      >>>     #show()

      >>> N = 16
      >>> z = zeros((N,N))

      >>> figure()
      >>> for i in arange(N*N):
      >>>     z.flat[i] = 0
      >>>     drawnow(draw_fig_real)
    """
    # replace the current figure w/o opening new GUI
    plt.clf()
    draw_fig(*argv, **kwargs)

    if show_once: plt.show()
    else: plt.draw_all()

    plt.pause(1e-3) # allows time to draw

    if confirm:
        string = raw_input('Hit <Enter> to continue ("d" for debugger and "x" to exit): ')
        if string == 'x' or string=='exit':
            sys.exit()
        if string == 'd' or string=='debug':
            print('\nType "exit" to continue program execution\n')
            pdb.runeval('u')

def figure(*args, **kwargs):
    """
    Enable drawnow. This function just enables interactivity then
    call's matplotlib's ion() to enable interactivity. Any arguments passed to
    this function are then passed to plt.figure()

    This function only enables interactivity and calls figure. To implement
    interactivity yourself, call plt.ion()

    Parameters
    ----------
    *argv    : any
               pass these arguments to plt.figure
    **kwargs : any
               pass these arguments to plt.figure
    """
    plt.ion()
    plt.figure(*args, **kwargs)

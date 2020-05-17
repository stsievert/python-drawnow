from __future__ import print_function
import sys
import pdb
import matplotlib.pyplot as plt


def drawnow(draw_fig, show_once=False, confirm=False, stop_on_close=False,
            *args, **kwargs):
    """A function to refresh the current figure.

    Depends on matplotlib's interactive mode. Similar functionality to MATLAB's
    drawnow.

    Parameters
    ----------
    draw_fig : callable
        The function that draws the figure you want to update
    show_once, optional : bool (default: False)
        If True, will call show() instead of draw().
    confirm, optional : bool, (default: False)
        If True, wait for user input after each iteration and present
        option to drop to python debugger (pdb).
    stop_on_close, optional : bool (default: False)
        When the figure is closed, stop the program execution.
    *args : list
        The list of parameters to pass ``draw_fig()``
    **kwargs : dict
        The keywords to pass to ``draw_fig()``

    Notes
    -----

    This function does not work with the inline plotting mode, which is
    common in Jupyter notebooks/lab, Spyder and the QTConsole. To
    disable this, run the following "magic" command:

        %matplotlib

    This will disable the Matplotlib inline mode and use the default plotting backend. For more detail, see `IPython's plotting documentation`_.

    Some limitations are the following:

    - Occaisonally ignores Ctrl-C especially while processing LaTeX.
    - The initial processing of Latex labels (typically on the x/y axis and
      title) is slow. However, matplotlib caches the results so any subsequent
      animations are pretty fast.
    - If two figures open and focus moved between figures, then other figure
      gets cleared.

    Usage Example
    -------------
      >>> from pylab import *  # import matplotlib before drawnow
      >>> from drawnow import drawnow, figure
      >>> def draw_fig_real():
      >>>     #figure() # don't call, otherwise opens new window
      >>>     imshow(z, interpolation='nearest')
      >>>     colorbar()
      >>>     #show()
      >>>
      >>> N = 16
      >>> z = zeros((N,N))
      >>>
      >>> figure()
      >>> for i in arange(N*N):
      >>>     z.flat[i] = 0
      >>>     drawnow(draw_fig_real)

    .. _IPython's plotting documentation: https://ipython.readthedocs.io/en/stable/interactive/plotting.html#id1

    """
    # replace the current figure w/o opening new GUI
    plt.clf()
    draw_fig(*args, **kwargs)

    if show_once:
        plt.show()
    else:
        plt.draw_all()

    plt.pause(1e-3)  # allows time to draw

    figures = plt.get_fignums()
    if stop_on_close and not figures:
        sys.exit()

    if confirm:
        string = raw_input('Hit <Enter> to continue, "d" for debugger and "x" '
                           'to exit: ')
        if string == 'x' or string == 'exit':
            sys.exit()
        if string == 'd' or string == 'debug':
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

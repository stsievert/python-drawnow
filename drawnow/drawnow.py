from matplotlib.pyplot import clf, show, draw
import matplotlib.pyplot as plt
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
    - If two figures open and focus moved between figures, then other figure
      gets cleared.

    Usage Example
    -------------
      >>> def draw_fig_real():
      >>>     #figure() # don't call, otherwise opens new window
      >>>     imshow(z, interpolation='nearest')
      >>>     colorbar()
      >>>     #show()

      >>> N = 16
      >>> z = zeros((N,N))

      >>> ion()
      >>> figure()
      >>> for i in arange(N*N):
      >>>     z.flat[i] = 0
      >>>     drawnow(draw_fig_real)
    """

    # unpacking kw args (found online)
    kw = dict()
    kw.update(kwargs)

    # replace the current figure w/o opening new GUI
    clf()
    draw_fig(*argv, **kw)

    if show_once: show()
    else: draw()
    if confirm: 
        string = raw_input('Hit <Enter> to continue, enter "d<Enter>" for \
                                debugger and "x" to exit: ')
        #if string == 'x':
            #break
        if string == 'd':
            print 'Type "exit" to continue program\n'
            pdb.runeval('u')

def figure(*args, **kwargs):
    """
    Enable drawnow. This function just enables interactivity then
    call's matplotlib's ion() to enable interactivity. Any arguments passed to
    this function are then passed to plt.figure()
    """
    plt.ion()
    plt.figure(*args, **kwargs)

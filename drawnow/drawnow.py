from matplotlib.pyplot import clf, show, draw

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

    Limitations
    -----------
    - If two figures open and focus moved between figures, then other figure
      gets cleared.
    - Occaisonally ignores Ctrl-C.

    Usage Example
    -------------
      >>> def draw_fig_real():
      >>>     imshow(z, interpolation='nearest')
      >>>     colorbar()
      >>> N = 16
      >>> z = zeros((N,N))

      >>> ion()
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
    if confirm: raw_input('Hit <Enter> to continue')

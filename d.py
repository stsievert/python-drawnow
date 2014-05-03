

from __future__ import division
from pylab import *
import time

def drawnow(draw_fig, show_once=False, *argv, **kwargs):
    """A function to refresh the current figure.

    Parameters
    ----------
    draw_fig : callable
               the function that draws the figure you want to update
    *argv    : any
               the list of parameters to pass ``draw_fig()``
    **kwargs : any
               the keywords to pass to ``draw_fig()``
    show_once, optional : bool, default: False. 
               If True, will call show() instead of draw(). 

    Limitations
    -----------
    - If two figures open and focus moved between figures, then other figure
      gets cleared.

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
    # get the kwargs
    kw = dict()
    kw.update(kwargs)

    # draw current figure
    clf()
    draw_fig(*argv, **kw)

    # should we show once? show() causes many windows to open, draw() doesn't
    if show_once:
        show()
    else:
        draw()


def drawnow_init():
    ion()

def draw_fig():
    figure()
    imshow(z, interpolation='nearest')
    #show()

def example():
    """
        must have the variables you're viewing be global: won't work with local
        vars.
    """

    global N, x, y, z
    N = 16
    x = linspace(-1, 1, num=N)
    x, y = meshgrid(x, x)
    z = x**2 + y**2


    drawnow_init()
    for i in arange(2*N):
        z.flat[i] = 0
        refresh(draw_fig)


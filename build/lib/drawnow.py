

from __future__ import division
from pylab import *
import time

def drawnow(draw_fig, wait_secs=1):
    """
        draw_fig: (callable, no args by use of python's global scope) your
        function to draw the figure. it should include the figure() call --
        just like you'd normally do it.  However, you must leave out the
        `show()`.

        wait_secs : optional, how many seconds to wait. note that if this is 0
        and your computation is fast, you don't really see the plot update.

        does not work in ipy-qt. only works in the ipython shell.
    """
    close()
    draw_fig()
    draw()
    time.sleep(wait_secs)

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
        drawnow(draw_fig)


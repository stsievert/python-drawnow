
from __future__ import division
from pylab import *
#from drawnow import drawnow

def draw_fig_real():
    imshow(z, interpolation='nearest')
    colorbar()
    print x, y, test

def drawnow(draw_fig, *argv, **kwargs):
    """A function to update 
    """
    # get the kwargs
    kw = dict()
    kw.update(kwargs)

    clf()
    draw_fig(*argv, **kw)
    draw()

N = 16
x = arange(N) #((N,N))
x, y = meshgrid(x, x)
z = (x-N/2)**2 + (y-N/2)**2

args = ()

ion()
for i in arange(N*N):
    z.flat[i] = 0
    drawnow(draw_fig_real)



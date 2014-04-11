
from __future__ import division
from pylab import *
from drawnow import drawnow, drawnow_init

def draw_fig_real():
    figure()
    imshow(z, interpolation='nearest')
    colorbar()

N = 16
x = arange(N) #((N,N))
x, y = meshgrid(x, x)
z = x**2 + y**3
z = ones((N,N))

drawnow_init()
for i in arange(N):
    z.flat[i] = 0
    drawnow(draw_fig_real)



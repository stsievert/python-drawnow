from __future__ import division
from pylab import zeros, arange, figure, ion, colorbar, imshow
from drawnow import drawnow

def draw_fig_real():
    imshow(z, interpolation='nearest')
    colorbar()

N = 16
z = zeros((N,N))

ion()
figure()
for i in arange(4*N):
    z.flat[i] = i+1
    drawnow(draw_fig_real, show_once=False, confirm=False)

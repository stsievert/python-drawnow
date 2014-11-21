from __future__ import division
#from pylab import zeros, arange, figure, ion, colorbar, imshow, plot, linspace, pi, sin, exp
from pylab import *
from drawnow import drawnow, figure
from scipy.special import jn
from time import sleep

def draw_fig():
    #figure() # don't call figure or show each time!
    imshow(x, interpolation='nearest')
    title('Iteration %d' % i)
    #show()

N = 10

seed(41)
figure(figsize=(4, 4))
x = eye(N) * 1 + randn(N,N) / 40
for i in arange(N):
    r = rand() + 0.3
    if r > 1: r = 1
    x[i, i-5] += r
    drawnow(draw_fig, confirm=False, show_once=False)
    sleep(0.1)

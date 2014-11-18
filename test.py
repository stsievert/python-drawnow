from __future__ import division
from pylab import zeros, arange, figure, ion, colorbar, imshow, plot, linspace, pi, sin
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *
import matplotlib.pyplot as plt
from drawnow import drawnow, figure

def draw_fig():
    #figure() # don't call figure or show each time!
    plot(t, x)
    #show()

N = 1e3
t = linspace(0, 2*pi, num=N)

figure(figsize=(8, 1))
for i in arange(300):
    x = sin(2*pi*t * i / 100.0 )
    drawnow(draw_fig, confirm=True)

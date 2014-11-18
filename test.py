from __future__ import division
from pylab import zeros, arange, figure, ion, colorbar, imshow, plot, linspace, pi, sin
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *
import matplotlib.pyplot as plt
from drawnow import drawnow, figure

#def t1():
def draw_fig():
    plot(t, x)

N = 1e3
t = linspace(0, 2*pi, num=N)

figure()
for i in arange(30):
    x = sin(2*pi*t * i / 100.0 )
    drawnow(draw_fig, confirm=True)

def t2():
    def draw_fig():

        # `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
        ax = fig.add_subplot(1, 2, 1, projection='3d')

        p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

        # surface_plot with color grading and color bar
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        cb = fig.colorbar(p, shrink=0.5)

    N = 1e3
    i = linspace(0, 1)
    X, Y = meshgrid(i, i)

    ion()
    fig = plt.figure(figsize=(14,6))
    for i in arange(10):
        Z = X**2 + Y**i
        drawnow(draw_fig)


from __future__ import division
from pylab import *
#from drawnow import drawnow

#t = linspace(0, 2*pi)
#x = sin(t)

#ion()
#figure()
#def f():
    #plot(x)
    ##show() 

#for i in linspace(0, 1):
    #x = sin(i*t)

    #f()
    #draw()
    ##drawnow(f)

import time
ion()
figure()
x = linspace(-1,1,51)
plot(sin(x))
for i in range(10):
    plot([sin(i+j) for j in x])
    # make it appear immediately
    draw()
    time.sleep(1)

<!--update with python setup.py upload-->

### `drawnow` for matplotlib

Matlab<sup>®</sup> has a great feature where it allows you to update a figure. You can
simply call `drawnow` and have your figure update. This is nice if you're
running a simulation and want to see the results every iteration. It'd sure be
nice if Python/matplotlib had a similar feature to update the plot each
iteration. This feature adds that functionality to matplotlib.

Example:

<img src="https://raw.githubusercontent.com/scottsievert/python-drawnow/master/example.gif" width="520" height="292"> 

Usage:
    
```python
from pylab import *
from drawnow import drawnow, figure
# plt.figure() must be imported before drawnow.figure()

x = zeros((N,N))

figure()
def function_to_draw_figure():
    #figure() # don't call, otherwise new window opened
    imshow(x) # python's global scope
    #show()   # don't call show()!

for i in arange(x):
    x.flat[i] = 1
    drawnow(function_to_draw_figure)
```

If you want to wait for confirmation after update or the option to drop into a
debugger, call `drawnow(function_to_draw_figure, confirm=True)`.

If you only want to show the figure once, call
`drawnow(function_to_draw_figure, show_once=True)`

### Installation
Two options:

1. Run `pip install drawnow`.
2. Download this repository and run `python setup.py install`.

#### Changes to code
This does require *small* changes to your code. All it should really amount
to is moving `figure(); plot(...); show()` inside a function; not much.

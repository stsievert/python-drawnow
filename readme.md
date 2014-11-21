<!--XXX: UPDATE WITH-->
<!--python setup.py build-->
<!--python setup.py sdist upload-->

### `drawnow` for matplotlib

The scientific community often runs iterative code, often in the form of
simulation. It's often useful to see the results after each iteration.
Accordingly, MATLAB<sup>®</sup> has a nice feature that allows you to update
the figure, `drawnow`. This bring the same feature to Python, with some extras.

Example:

<img src="tests/test.gif">

<!--width="520" height="292"> -->

This is shown with `imshow`, but python-drawnow allows updates of any figure.

Usage:
    
```python
from pylab import *
from drawnow import drawnow, figure
# if imported into the global namespace, plt.figure() must be imported
# before drawnow.figure()

figure()
def function_to_draw_figure():
    #figure() # don't call, otherwise new window opened
    imshow(x, interpolation='nearest') # python's global scope
    #show()   # don't call show()!

N = 10
x = zeros((N,N))
for i in arange(N):
    x[i, i] = 1
    drawnow(function_to_draw_figure)
```

If you want to wait for confirmation after update or the option to drop into a
debugger, call `drawnow(function_to_draw_figure, confirm=True)`.

If you only want to show the figure once, call
`drawnow(function_to_draw_figure, show_once=True)`

The full documentation is included in the doc strings.

### Installation
Two options:

1. Run `pip install drawnow`.
2. Download this repository and run `python setup.py install`.

#### Changes to code
This does require *small* changes to your code. All it should really amount
to is moving `figure(); plot(...); show()` inside a function; not much.

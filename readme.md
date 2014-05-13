
### `drawnow` for matplotlib

Matlab<sup>®</sup> has a great feature where it allows you to update a figure. You can
simply call `drawnow` and have your figure update. This is nice if you're
running a simulation and want to see the results every iteration. It'd sure be
nice if Python/matplotlib had a similar feature to update the plot each
iteration. This feature adds that functionality to matplotlib.

Example:

<!--![example][ex]-->

<img src="https://raw.githubusercontent.com/scottsievert/python-drawnow/master/example.gif" width="520" height="292"> 

<!--[ex]:https://raw.githubusercontent.com/scottsievert/python-drawnow/master/example.gif-->


Usage:
    
```python
from drawnow import drawnow

x = zeros((N,N))

def function_to_draw_figure():
    #figure() # don't call, otherwise new window opened
    imshow(x) # python's global scope
    #show()   # don't call show()!

ion() # enable interactivity, can be default
figure()
for i in arange(x):
    x.flat[i] = 1
    drawnow(function_to_draw_figure)
```

If you want to wait for confirmation after update, call `drawnow(function_to_draw_figure, confirm=True)`.

If you only want to show the figure once, call
`drawnow(function_to_draw_figure, show_once=True)`

### Installation
Two options:

1. Download this repository and run `python setup.py install`.
2. Run `pip install drawnow`.

#### Changes to code
This does require *small* changes to your code. All it should really amount
to is moving `figure(); plot(...); show()` inside a function; not much.

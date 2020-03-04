``drawnow`` for matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~

Matlab has a great feature where it allows you to update a figure. You can
simply call `drawnow` and have your figure update. This is nice if you're
running a simulation and want to see the results every iteration. It'd sure be
nice if Python/matplotlib had a similar feature to update the plot each
iteration. This package adds that functionality to matplotlib.

This readme is probably out of date; a more complete file is on Github.

Usage:
    
.. code:: python

    # Trimmed version of test.py
    from pylab import *
    from drawnow import *

    def approx(x, k):
        ...

    figure(...)
    def draw_fig():
        """ Uses Python's global scope """
        subplot(1, 2, 1)
        imshow(x, cmap='gray')
        # ...

        subplot(1, 2, 2)
        imshow(x_hat, cmap='gray')
        # ...
        # show()

    x = imread('test-data/mandrill.png')
    k_values = around(logspace(0.1, log10(64), num=10)).astype('int')
    for k in k_values:
        x_hat = approx(x, k)
        drawnow(draw_fig, stop_on_close=True)

If you want to wait for confirmation after update, call ``drawnow(function_to_draw_figure, confirm=True)``.

If you only want to show the figure once, call
``drawnow(function_to_draw_figure, show_once=True)``

Installation
~~~~~~~~~~~~
Two options:

1. Download this repository and run `python setup.py install`.
2. Run ``pip install drawnow``.



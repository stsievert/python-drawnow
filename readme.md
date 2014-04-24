
### `drawnow` for matplotlib

Usage:
    
    from drawnow import drawnow, drawnow_init
    drawnow_init()
    x = zeros((N,N))

    def function_to_draw_figure():
        figure()
        imshow(x) # python's global scope
        #show()   # don't call show()!

    for i in arange(x):
        x.flat[i] = 1
        drawnow(function_to_draw_figure)

### Installation
1. Download this repository.
2. Put `drawnow.py` in your current folder or the drawnow folder in
   `../python/site-packages/`.

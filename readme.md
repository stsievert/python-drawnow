
### `drawnow` for matplotlib

Usage:
    
    `drawnow_init()`
    x = zeros((N,N))

    def function_to_draw_figure():
        figure()
        imshow(x) # python's global scope
        #show()   # don't call show()!

    for i in arange(x):
        x.flat[i] = 1
        drawnow(function_to_draw_figure)

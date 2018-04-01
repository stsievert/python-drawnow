from __future__ import division
from pylab import *
from scipy.sparse.linalg import svds
from drawnow import *

def approx(x, k):
    """ Approximate x using the SVD keeping the k largest singular values. """
    y = zeros_like(x)
    for i in arange(4):
        u, sigmas, v = svd(x[:,:,i])
        sigmas[k:] = 0

        s = zeros_like(x[:,:,i])
        fill_diagonal(s, sigmas)

        color = u.dot(s).dot(v)
        y[:,:,i] = np.clip(color, 0, 1)
    return y

WIDTH = 7
figure(figsize=(WIDTH, WIDTH / 2))
def draw_fig():
    """ Uses Python's global scope """
    subplot(1, 2, 1)
    imshow(x, cmap='gray')
    title('Original')
    axis('off')

    subplot(1, 2, 2)
    imshow(x_hat, cmap='gray')
    title('Approx with $k=%d$' % k)
    axis('off')
    # show()

x = imread('test-data/mandrill.png')
k_values = around(logspace(0.1, log10(64), num=10)).astype('int')
for k in k_values:
    x_hat = approx(x, k)
    drawnow(draw_fig, stop_on_close=True)

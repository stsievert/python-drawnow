clc; clear all; close all;

N = 16;
x = zeros(N,N);

figure()
imshow(x)
%function_to_draw()

for i=1:N*N,
    x(i) = i;
    
    imshow(x)
    %function_to_draw()
    
    drawnow
    pause(0.01)
end
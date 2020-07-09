from skimage.transform import (hough_line, probabilistic_hough_line)
from skimage.feature import canny
from skimage import io, color

img = io.imread("image.jpg")
img = color.rgb2gray(img)

edge = canny(img, 2, 1, 25)

lines = hough_line(img)
probabilistic_lines = probabilistic_hough_line(edge, threshold = 10, line_length = 5, line_gap = 3)

io.imshow(edge)
io.imsave("canny_edge_hough.jpg", edge)
io.show()

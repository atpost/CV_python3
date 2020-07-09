#Program to convert a color image to grayscale image 

from skimage import color, io 

#Read an image from a file
img = io.imread('image.png')

#Convert the image tp grayscale
hsv_image = color.rgb2hsv(img)

io.imshow(hsv_image)
io.show()

'''
  File "skimage_rgb_hsv.py", line 9, in <module>
    hsv_image = color.rgb2hsv(img)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python37\lib\site-packages\skimage\color\colorconv.py", line 253, in rgb2hsv
    arr = _prepare_colorarray(rgb)
  File "C:\Users\ASUS\AppData\Local\Programs\Python\Python37\lib\site-packages\skimage\color\colorconv.py", line 150, in _prepare_colorarray
    raise ValueError("Input array must have a shape == (..., 3)), "
ValueError: Input array must have a shape == (..., 3)), got (383, 383, 4)
'''

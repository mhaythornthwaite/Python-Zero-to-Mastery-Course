# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:02:12 2020

@author: mhayt
"""

print(f'\n\n')
print(' ---------------- START ---------------- ')

#-------------------------------- SCRIPTING ----------------------------------

#----------------------------- IMAGE PROCESSING ------------------------------


from PIL import Image, ImageFilter

#created a pillow object 
img = Image.open('./Pokedex/pikachu.jpg')

#printing attributes of the image class
print(img)
print(img.format)
print(img.size)
print(img.mode)

#Finding the methods that are available to the image class.
#print(dir(img))

#In the module Image, there is a method called .filter() The ImageFilter module contains definitions for a pre-defined set of filters which can be used in conjunction with the aforementioned .filter() method.

'''
Available Filters

BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SHARPEN
SMOOTH
SMOOTH_MORE

'''

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./Filtered_Images/blur.png', 'png')

filtered_img = img.filter(ImageFilter.FIND_EDGES)
filtered_img.save('./Filtered_Images/edges.png', 'png')

filtered_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
filtered_img.save('./Filtered_Images/edge_enhance_more.png', 'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('./Filtered_Images/sharpen.png', 'png')


#Converting to Greyscale just with .convert rather than .filter(filter_type)

filtered_img = img.convert('L')
filtered_img.save('./Filtered_Images/grey.png', 'png')


#converts rgb to CIE XYZ color space

rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0 )
filtered_img = img.convert("RGB", rgb2xyz)
filtered_img.save('./Filtered_Images/rgb2xyz.png', 'png')

#filtered_img.show()

rotate_img = img.rotate(90) #90 degrees anticlockwise
rotate_img.save('./Filtered_Images/rotate.png', 'png')

resize_img = img.resize((300,300)) #resizes to set pixel amount
resize_img.save('./Filtered_Images/resize.png', 'png')

crop_img = img.crop((0,0,300,300)) #takes tuple input
crop_img.save('./Filtered_Images/crop.png', 'png')


print('\n')
#----------------------------- ASTRO EXCERSISE -------------------------------


img = Image.open('./astro.jpg')

print(img.size)

resize_img = img.resize((300,300))
resize_img.save('./resize_astro.png', 'png')



# -------- CREATING OWN IMAGE SIZE REDUCTION FUNCTION --------


def Image_Resize(Image, Reduction_factor):
    '''
    Image = instantiated image file -> Image.open(<file_location>)
    Reduction_factor -> a factor of 2 will reduce a 800*600 image to 400*300
    '''
    img_size_t = Image.size
    img_size_l = list(img_size_t)
    img_resize_l = []
    for i in img_size_l:
        x = int(i / Reduction_factor)
        img_resize_l.append(x)
    img_resize = tuple(img_resize_l)
    resize_img = Image.resize(img_resize)
    return resize_img
  
img_astro = Image.open('./astro.jpg')

Image_Resize(img_astro, 5).save('./test.png', 
                                'png')


#someones already done this with thumbnail. This retains aspect ration and you define the largest x and y can be. see code below:
#img.thumbnail((400,400))
#img.save('./thumbnail.png')


print('\n')
#--------------------------- JPG TO PNG EXCERSISE ----------------------------








# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print(f'\n')



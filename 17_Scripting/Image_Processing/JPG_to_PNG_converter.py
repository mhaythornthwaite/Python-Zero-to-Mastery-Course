# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:59:19 2020

@author: mhayt
"""


print('\n\n')
print(' ---------------- START ---------------- ')

#---------------------------- JPG TO PNG CONVERTER ----------------------------

'''

TASK

$ JPG_to_PNG_converter.py Pokedex/ new/

so we need to grab the first and second argument with sys.

we need to check if folder: new/ exists, if not create it.

loop through Pokedex/
convert to PNG
move to new/ folder

'''

# =============================================================================
# To run file use the following command in the console:
# 
# runfile('JPG_to_PNG_converter.py', args='Pokedex PNG_Images')
# =============================================================================

import sys
import os
from PIL import Image

input_dir = f'./{sys.argv[1]}'
output_dir = f'./{sys.argv[2]}'

print(input_dir)
print(output_dir)


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for im in os.listdir(input_dir):
    if im.endswith(".jpg"):
        im_instantiate = Image.open(f'{input_dir}/{im}')
        rgb_im = im_instantiate.convert('RGB')
        new_name = im[:-4]
        rgb_im.save(f'{output_dir}/{new_name}.png', 'png')




# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
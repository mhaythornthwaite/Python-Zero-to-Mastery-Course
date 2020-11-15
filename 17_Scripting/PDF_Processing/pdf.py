# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:39:17 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- ')

#------------------------------------ PDF -------------------------------------

import PyPDF2

path = './PDF_Playground'


# =============================================================================
# note the mode is rb which is read binary
# also note in the code below PdfFileReader is a class -> it initializes a PdfFileReader object and we can then call attributes from it such a numPages
# =============================================================================


with open(f'{path}/dummy.pdf', 'rb') as file:
    print(file)
    print(type(file), '\n')
    reader = PyPDF2.PdfFileReader(file) #instantiate as a new class
    print(reader)
    print(type(reader), '\n')
    print(reader.numPages)



with open(f'{path}/twopage.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page1 = reader.getPage(0)
    page1.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page1)
    with open(f'{path}/rotated_page.pdf', 'wb') as new_file:
        writer.write(new_file)
    


# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
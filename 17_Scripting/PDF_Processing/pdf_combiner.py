# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:21:26 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- ')

#-------------------------------- PDF COMBINER --------------------------------

# =============================================================================
# To run file use the following command in the console:
# 
# runfile('pdf_combiner.py', args='dummy.pdf twopage.pdf wtr.pdf')
# =============================================================================


import sys
import PyPDF2

inputs = sys.argv[1:]

def pdf_comb(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super_merge.pdf')

pdf_comb(inputs)




# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
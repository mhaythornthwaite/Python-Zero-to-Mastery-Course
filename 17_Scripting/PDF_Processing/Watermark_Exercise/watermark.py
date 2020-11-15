# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:27:09 2020

@author: mhayt
"""

print('\n\n')
print(' ---------------- START ---------------- ')

#----------------------------- WATERMARK EXERCISE -----------------------------

import PyPDF2

#names of the pdf files to merge
input_pdf = 'super_merge.pdf'
wtr_mark = 'wtr.pdf'


#opening the watermark as a PdfFileReader class and then getting the first page
watermark = PyPDF2.PdfFileReader(open(wtr_mark, 'rb'))
watermark_page = watermark.getPage(0)


#opening the pdf as a PdfFileReader class
pdf = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))


#creating an empty PdfFileWriter object ready to output the merge to
pdf_writer = PyPDF2.PdfFileWriter()



# =============================================================================
# good lesson this, when we do for loops we really need to think about what we're wanting to loop through. Here we're wanting to loop through the pages of our PDF, but our loop isnt actully doing this. Our loop is just going from 0 to the total number of pages: so 0, 1, 2, 3. Actully our function produces range(0, 4) which is [0, 1, 2, 3, 4] which is one more page than we have but as this last iteration has no page nothing happens so it does not cause an issue. We're then making it iterate through the pages with pdf_page = pdf.getPage(page). Note the in ...: needs to be an iterable, so a list or a range function. 

print(range(pdf.getNumPages()))
# =============================================================================



for page in range(pdf.getNumPages()):
    
    #opening page 
    pdf_page = pdf.getPage(page)
    
    #merging page with the watermark page(that were not iterating over)
    pdf_page.mergePage(watermark_page)
    
    #adding the merged page to the writer object
    pdf_writer.addPage(pdf_page)  


#formally saving the pdf_writer object which is stored locally during the running of the script to an output pdf file.
with open('output.pdf', 'wb') as fh:
    pdf_writer.write(fh)




# =============================================================================
# Lets make this into a nice looking function
# =============================================================================


def Watermark(input_pdf, watermark_pdf, output_pdf):
    '''
    Please specify pdf documents in the same location as this function is located. Please also specificy the name of the output pdf, e.g. edited.pdf
    '''
    
    watermark = PyPDF2.PdfFileReader(open(watermark_pdf, 'rb'))
    watermark_page = watermark.getPage(0)

    pdf = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
    pdf_writer = PyPDF2.PdfFileWriter()

    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)  

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)


Watermark('super_merge.pdf', 'wtr.pdf', 'import_test.pdf')







# ---------------------------------- END -------------------------------------

print(' ----------------- END ----------------- ')
print('\n')
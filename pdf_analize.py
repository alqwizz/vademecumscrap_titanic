import os
import sys

import fitz
from tika import parser
import PyPDF2

# rawText = parser.from_file('file.pdf')
# print(str(rawText))
reader = PyPDF2.PdfFileReader('file.pdf')
print(str(reader.documentInfo))

doc = fitz.open("file.pdf")

for i in range(len(doc)):
    print('')
    print ('-> PAGINA n.' + str(i))
    print (str(doc.getPageImageList(i)))
    cont = 0
    for img in doc.getPageImageList(i):
        cont = cont + 1
        print('  -Imagen ' + str(cont))
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:  # this is GRAY or RGB
            pix.writePNG("p%s-%s.png" % (i, xref))
        else:  # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None
print('')
print('-----------------------------')
print('IMAGENES EXTRAIDAS CON EXITO')
print('')


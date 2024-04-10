#!/usr/bin/python
# vim: set fileencoding=<UTF-8> :

from PyPDF2 import PdfReader, PdfWriter

pdfIn = open("in.pdf", "rb")  # exchange the 'original.pdf' with a name of your file
pdfReader = PdfReader(pdfIn)
pdfWriter = PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    page = pdfReader.pages[pageNum]
    page.rotate(90)
    pdfWriter.add_page(page)

pdfOut = open("out_rotated.pdf", "wb")
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()

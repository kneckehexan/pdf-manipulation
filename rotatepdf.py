from PyPDF2 import PdfReader, PdfWriter

pdfIn = open("2.pdf", "rb")  # exchange the 'original.pdf' with a name of your file
pdfReader = PdfReader(pdfIn)
pdfWriter = PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    page = pdfReader.pages[pageNum]
    page.rotate(90)
    pdfWriter.add_page(page)

pdfOut = open("rotated.pdf", "wb")
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()

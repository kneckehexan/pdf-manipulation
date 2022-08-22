from PyPDF2 import PdfFileReader, PdfFileWriter

def main():
    path = input('Name of pdf, including extension: ')
    name = input('Name of the split: ')
    split(path, name)


def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


if __name__ == '__main__':
    main()

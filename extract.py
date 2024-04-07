import os

from PyPDF2 import PdfFileMerger, PdfReader, PdfWriter


def main():

    file_name = input("Enter the name of the PDF file: ").strip()
    no_pages = int(input("Enter the number of pages: "))

    if not os.path.isfile(file_name):
        print(f"The file {file_name} does not exist.")
    else:
        inputpdf = PdfReader(open(file_name, "rb"))

        for i in range(0, no_pages):
            writer = PdfWriter()
            writer.add_page(inputpdf.pages[i])
            with open("%s-page%s.pdf" % (file_name, i), "wb") as output_pdf:
                writer.write(output_pdf)

        # Merge the split PDF files
        # merge_pdf = PdfFileMerger()

        # for i in range(0, 6):
        #    merge_pdf.append(open("%s-page%s.pdf" % (file_name, i), "rb"))

        # with open("merged_%s" % file_name, "wb") as output_pdf:
        #    merge_pdf.write(output_pdf)


if __name__ == "__main__":
    main()

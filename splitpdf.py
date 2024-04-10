import os

from PyPDF2 import PdfReader, PdfWriter


def main():
    with open("in.pdf", "rb") as infile:
        reader = PdfReader(infile, strict=False)
        page = 0
        writer = PdfWriter()
        total_pages = len(reader.pages)
        while page < total_pages:
            writer.add_page(reader.pages[page])
            if page == int(total_pages / 3) or page == total_pages - 1:
                with open("out-{}.pdf".format(page), "wb") as outfile:
                    writer.write(outfile)
                    writer = PdfWriter()
            page += 1


if __name__ == "__main__":
    main()

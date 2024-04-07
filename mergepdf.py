import os

from PyPDF2 import PdfMerger


def main():
    pdfFiles = []  # variable

    for root, dirs, filenames in os.walk(os.getcwd()):  # Root and directory pathway.
        for filename in filenames:
            if filename.lower().endswith(".pdf"):
                pdfFiles.append(os.path.join(root, filename))
                # Appending files to root name from OS (operating system).

    pdfFiles.sort()
    print(pdfFiles)
    merger = PdfMerger()
    for pdf in pdfFiles:
        merger.append(pdf)

    merger.write("merge.pdf")


if __name__ == "__main__":
    main()

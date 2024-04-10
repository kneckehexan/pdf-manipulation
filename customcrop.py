from pypdf import PdfReader, PdfWriter

"""
Custom croppping, assuming all content is pushed to the top left corner.
"""

with open("in.pdf", "rb") as in_f:
    input1 = PdfReader(in_f)
    output = PdfWriter()

    page = input1.pages[0]
    print("lower left:", page.cropbox.lower_left)
    print("lower right:", page.cropbox.lower_right)
    print("upper left:", page.cropbox.upper_left)
    print("upper right:", page.cropbox.upper_right)

    lower_right_x = int(input("Length in pixels, left to right: "))
    lower_right_y = int(input("Lenght in pixels, top to bottom: "))

    lower_left_y = lower_right_y
    lower_left_x = 0

    upper_right_x = lower_right_x
    upper_right_y = 0

    upper_left_x = 0
    upper_left_y = 0

    page.mediabox.lower_right = (
        lower_right_x,
        lower_right_y,
    )
    page.mediabox.lower_left = (
        lower_left_x,
        lower_left_y,
    )
    page.mediabox.upper_right = (
        upper_right_x,
        upper_right_y,
    )
    page.mediabox.upper_left = (
        upper_left_x,
        upper_left_y,
    )

    output.add_page(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)

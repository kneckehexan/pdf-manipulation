from pypdf import PdfReader, PdfWriter

"""
Works for cropping scanned A4 page (600 DPI) down to a somewhat regular business card
"""

with open("in.pdf", "rb") as in_f:
    input1 = PdfReader(in_f)
    output = PdfWriter()

    page = input1.pages[0]
    # print(page.cropbox.lower_left)
    # print(page.cropbox.lower_right)
    # print(page.cropbox.upper_left)
    # print(page.cropbox.upper_right)

    x = 250
    y = 690

    upper_right_new_x_coordinate = x
    lower_left_new_y_coordinate = y

    lower_left_new_x_coordinate = 0
    upper_right_new_y_coordinate = 841
    upper_left_new_x_coordinate = 0
    upper_left_new_y_coordinate = 841

    page.mediabox.lower_right = (
        x,
        y,
    )
    page.mediabox.lower_left = (
        lower_left_new_x_coordinate,
        lower_left_new_y_coordinate,
    )
    page.mediabox.upper_right = (
        upper_right_new_x_coordinate,
        upper_right_new_y_coordinate,
    )
    page.mediabox.upper_left = (
        upper_left_new_x_coordinate,
        upper_left_new_y_coordinate,
    )

    output.add_page(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)

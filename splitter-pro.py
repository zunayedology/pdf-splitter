import PyPDF2 as pdf
import pandas as pd

def split_pdf(input_file, excel_file, output_folder):
    # Read Excel sheet
    df = pd.read_excel(excel_file)

    with open(input_file, 'rb') as file:
        pdf_reader = pdf.PdfReader(file)

        page = pdf_reader.pages[0]
        page_width = page.mediabox.width
        page_height = page.mediabox.height

        # Calculate dimensions for four equal parts
        part_width = page_width / 2
        part_height = page_height / 2

        # Iterate through people in the Excel sheet
        for i, (name, receipt_number, date) in df.iterrows():
            pdf_writer = pdf.PdfWriter()
            pdf_writer.add_page(page)

            # Set new dimensions for the part
            x0 = i % 2 * part_width
            y0 = int(i / 2) * part_height

            pdf_writer.pages[0].mediabox.lower_left = (x0, y0)
            pdf_writer.pages[0].mediabox.upper_right = (x0 + part_width, y0 + part_height)

            # Construct output file name
            output_file = f"{output_folder}\AD Receipt_{name}_({receipt_number})_{date}.pdf"

            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
                print(f"Part {i + 1} saved to {output_file}")

        print("DONE!")

input_file_path = "input_0001.pdf"
excel_file_path = "table.xlsx"
output_folder_path = "output"

split_pdf(input_file_path, excel_file_path, output_folder_path)

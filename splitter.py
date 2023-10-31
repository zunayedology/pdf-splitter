import PyPDF2

def split_pdf(input_file, output_prefix):
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        if total_pages != 1:
            print("Input PDF should have exactly 1 page.")
            return

        page = pdf_reader.pages[0]
        page_width = page.mediabox.width
        page_height = page.mediabox.height

        # Calculate dimensions for four equal parts
        part_width = page_width / 2
        part_height = page_height / 2

        # Create and save each part as a new PDF file
        for i in range(4):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)

            # Set new dimensions for the part
            x0 = i % 2 * part_width
            y0 = int(i / 2) * part_height

            pdf_writer.pages[0].mediabox.lower_left = (x0, y0)
            pdf_writer.pages[0].mediabox.upper_right = (x0 + part_width, y0 + part_height)
        
            output_file = f"output/{output_prefix}_part{i + 1}.pdf"

            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
                print(f"Part {i + 1} saved to {output_file}")

# Replace 'input.pdf' with the path to your input PDF file
input_file_path = "input\one-page-doc.pdf"
# Replace 'output_prefix' with the desired prefix for the output files
output_prefix = 'output'

split_pdf(input_file_path, output_prefix)

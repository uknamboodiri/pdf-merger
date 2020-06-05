# https://pythonhosted.org/PyPDF2/
import PyPDF2
import sys

with open("./pdfs/dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader)

    page = reader.getPage(0)
    page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("./pdfs/tilt.pdf", "wb") as new_file:
        writer.write(new_file)

# merge 2 pdf files
#     take inputs and merge all files

    pdf_list = sys.argv[1:]
    merged_file = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        # print(pdf)
        merged_file.append(pdf)

    merged_file.write("./pdfs/merged_files.pdf")


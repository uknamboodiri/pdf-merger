import PyPDF2
import sys

input = sys.argv[1]
template = sys.argv[2]

input_file = PyPDF2.PdfFileReader(open(input, "rb"))
template_file = PyPDF2.PdfFileReader(open(template, "rb"))
output_file = PyPDF2.PdfFileWriter()

for pg_number in range(input_file.getNumPages()):
    page = input_file.getPage(pg_number)
    page.mergePage(template_file.getPage(0))
    output_file.addPage(page)

with open("./pdfs/water_marked.pdf", "wb") as file:
    output_file.write(file)

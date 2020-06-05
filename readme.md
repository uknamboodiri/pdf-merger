# pdf-merger

Program to merge or water mark pdf files

##Merge
Usage:
python merge.py <file1> <file2> <file3> <file4> ....

output:
./pdfs/merged_files.pdf

Example:
python merge.py ./pdfs/dummy.pdf ./pdfs/twopage.pdf

##water mark pdf files

Usage:
python water_mark.py <file_to_water_mark> <water_mark_template_file> 

output:
./pdfs/water_marked.pdf

Example:
python3.8 water_mark.py ./pdfs/merged_files.pdf ./pdfs/wtr.pdf 


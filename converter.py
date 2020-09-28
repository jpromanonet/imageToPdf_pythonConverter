# Calling all libraries needed
#-------------------------------
# Install the following libraries:
#   pip install fpdf
#-------------------------------
from os import listdir
from fpdf import FPDF

# Ask the user to Path to convert
path = input("Introduce la ruta para convertir: ")

# Processing images to PDF
imageList = listdir(path)
imageList.sort()

# Convert to PDF with a default A4 Size
pdfFile = FPDF('P', 'mm', 'A4')

# Now we define the axis
x = 0
y = 0
w = 210
h = 297

# Adding images to the PDF file in one bundle
for image in imageList:
    pdfFile.add_page()
    pdfFile.image(path+image,x,y,w,h)

pdfFile.output("documentoFinal.pdf","F")
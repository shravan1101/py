from pypdf import PdfWriter
import os

merger = PdfWriter()
files = os.listdir()

for file in files:
    if file.endswith(".pdf"):
        merger.append(file)
        
merger.write("merged-pdf.pdf")
merger.close()

# # print(files)
# for pdf in files:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()

# from pypdf import PdfWriter
# import os

# merger = PdfWriter()

# # Get list of all PDF files in current directory
# pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

# # Sort the files alphabetically (optional but useful)
# pdf_files.sort()

# # Append each PDF to the merger
# for pdf in pdf_files:
#     merger.append(pdf)

# # Write to output file
# merger.write("merged-pdf.pdf")
# merger.close()


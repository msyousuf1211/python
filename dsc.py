import tabula

# Convert PDF to Excel
tabula.convert_into(" merit list xlsx.pdf", "dsc.xlsx", output_format="xlsx", pages='all')
print("PDF converted to Excel successfully!")

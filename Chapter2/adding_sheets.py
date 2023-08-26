import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Add a new sheet
workbook.create_sheet(title="Sheet2")

# Save the changes
workbook.save("example.xlsx")

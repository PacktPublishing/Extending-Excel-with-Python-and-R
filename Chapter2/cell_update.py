import openpyxl

# Load an existing workbook
workbook = openpyxl.load_workbook("example.xlsx")

# Add a new sheet
workbook.create_sheet(title="Sheet1")

# Select a sheet
sheet_name = "Sheet1"

sheet = workbook[sheet_name]

# Update a cell value
sheet["A1"] = "Hello, World!"

# Save the changes
workbook.save("example.xlsx")

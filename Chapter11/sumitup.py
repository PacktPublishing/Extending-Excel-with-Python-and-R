import xlwings as xw


def main():
    wb = xw.Book.caller()
    a = wb.sheets[0]['A1'].value
    b = wb.sheets[0]['A2'].value
    wb.sheets[0]['A3'].value = a + b
    pass

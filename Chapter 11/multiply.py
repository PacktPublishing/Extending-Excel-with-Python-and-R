import xlwings as xw


def main():
    wb = xw.Book.caller()
    a = wb.sheets[0]['A1'].value
    b = wb.sheets[0]['B1'].value
    wb.sheets[0]['C1'].value = a * b
    pass

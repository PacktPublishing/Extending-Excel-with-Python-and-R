import xlwings as xw 


def helloworld(): 

    wb = xw.Book.caller() 

    wb.sheets[0]['A1'].value = 'Hello World!' 
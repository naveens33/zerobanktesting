import xlrd

def getData(filename,sheetname):
    wb=xlrd.open_workbook("testdata\\"+filename)
    sheet = wb.sheet_by_name(sheetname)
    print(sheet.nrows,sheet.ncols)
    data = []
    for i in range(1,sheet.nrows):
        temp = []
        for j in range(sheet.ncols):
            temp.append(sheet.cell_value(i,j))
        data.append(temp)
    return data

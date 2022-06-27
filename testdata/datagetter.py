import xlrd


def getData(file_path,sheet_name):
    data = []
    wb = xlrd.open_workbook('C:\\Users\\Naveen S\\PycharmProjects\\zerobank\\testdata\\'+file_path)
    sh = wb.sheet_by_name(sheet_name)
    for i in range(1, sh.nrows):
        li = []
        for j in range(0, sh.ncols):
            li.append(sh.cell_value(i, j))
        data.append(li)
    return data

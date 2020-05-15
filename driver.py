from gray import Library
import xlrd 
import pandas as pd
import numpy as np

file = r'C:\Users\bgethe\Downloads\Code_repository\Local_language\Umlaut_Foreign_characters\sample.xlsx'
ofile = r'C:\Users\bgethe\Downloads\Code_repository\Local_language\Umlaut_Foreign_characters\sample_out.xlsx'

print("READING DATA",end='\r')
gray = Library()
colnames = [] # column names will be stored here
data = [] # all data is stored here in list of rows format


wb = xlrd.open_workbook(file) 
sheet = wb.sheet_by_index(0) 
columnLen = sheet.ncols
colnames = sheet.row_values(0)

for i in range(1,sheet.nrows):
    dat = sheet.row_values(i)
    data.append(dat)

del sheet
del wb
print('Done Reading Data')

print("Processing Data",end='\r')
cdata = []
edata = []
fdata = []
for i in range(len(data)):
    lst = data[i]
    tcd = []
    ted = []
    isEng = True
    for ls in lst:
        ls = str(ls) # converting cell value to string
        clean = gray.cleanString(ls) # cleaning the string
        eng = gray.parseToEnglish(clean) # converting string to english by parsing known umlauts
        if gray.hasForeign(eng): # check if it contains a foreign character
            isEng = False # if foreign character present in cell then this row will not go to english sheet
        tcd.append(clean)
        ted.append(eng)
    cdata.append(tcd) # add all clean data to clean sheet
    if isEng:
        edata.append(ted) # if complete row is english then add this row to english sheet
    else:
        fdata.append(ted) # else add the row to foreign sheet
print("Done Processing Data")

print("Writing Data",end='\r')
df0 = pd.DataFrame(np.array(cdata),columns=colnames)
df1 = pd.DataFrame(np.array(edata),columns=colnames)
df2 = pd.DataFrame(np.array(fdata),columns=colnames)
with pd.ExcelWriter(path=ofile,mode='w+') as f:
    df0.to_excel(excel_writer=f,sheet_name="CLEANED",encoding='utf-8')
    df1.to_excel(excel_writer=f,sheet_name="ENGLISH",encoding='utf-8')
    df2.to_excel(excel_writer=f,sheet_name="FOREIGN",encoding='utf-8')
print("Done Writing Data")

"""
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44
50 51 52 53 54
60 61 62 63 64
70 71 72 73 74
"""
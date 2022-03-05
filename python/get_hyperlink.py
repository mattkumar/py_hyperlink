import openpyxl
import pandas 

# path:  path to physical xlsx workbook file
# sheet: sheet of interest within the workbook
# source_col: the column index the sheet where hyperlinks are to be extracted from
# target_col: the column index the sheet where the hyperlinks are to be stored

def get_hyperlink(path, sheet, source_col, target_col):

  workbook = openpyxl.load_workbook(path)
  worksheet= workbook.get_sheet_by_name(sheet)
  
  for i in range(1, worksheet.max_row+1):
    cellref = worksheet.cell(column = int(target_col), row = i)
    try:
      cellref.value = worksheet.cell(column = int(source_col), row = i).hyperlink.target
    except:
      cellref.value = worksheet.cell(column = int(source_col), row = i).value

  # workbook.save(path)
  df = pandas.DataFrame(worksheet.values)
  return df


 

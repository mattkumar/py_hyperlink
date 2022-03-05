import openpyxl
import pandas as pd

def get_hyperlink(path):

  workbook = openpyxl.load_workbook(path)
  worksheet= workbook.get_sheet_by_name('Sheet1')
  
  for i in range(1, worksheet.max_row+1):
    cellref = worksheet.cell(column = 3, row = i)
    try:
      cellref.value = worksheet.cell(column = 2, row = i).hyperlink.target
    except:
      cellref.value = worksheet.cell(column = 2, row = i).value

  # workbook.save(path)
  df = pd.DataFrame(worksheet.values)
  return df


 

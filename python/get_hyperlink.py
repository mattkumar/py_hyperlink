import openpyxl as xl
import pandas as pd

def get_hyperlink(path, sheet):

  # Define workbook, worksheet
  wb = xl.load_workbook(path)
  ws = wb.get_sheet_by_name(sheet)
  
  # For all cells in the worksheet, if a hyperlink is detected, extract the hyperlink target 
  # Otherwise just keep the original value as a string
  for row_cells in ws.iter_rows():
    for cell in row_cells:
      try:
        cell.value = cell.hyperlink.target
      except:
        cell.value = str(cell.value)
    
  # Store values to a data frame, clean up headers 
  tmp = pd.DataFrame(ws.values)
  tmp.rename(columns = tmp.iloc[0], inplace = True)
  tmp.drop(tmp.index[0], inplace = True)
  
  return tmp
  


 

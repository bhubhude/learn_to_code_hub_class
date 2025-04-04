# import openpyxl
# from openpyxl import  Workbook, load_workbook
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

# wb = openpyxl.load_workbook("bhubhude_excel_file.xlsx")
# sheet = wb["Table1"]
# # print(sheet)
# for row in sheet.iter_rows():
#     for cell in row:
#         print(cell.value)

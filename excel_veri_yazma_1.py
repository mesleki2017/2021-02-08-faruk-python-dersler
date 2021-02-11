from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet.cell(row=1, column=1).value = "cesur"

workbook.save(filename="veriyazdim.xlsx")

import openpyxl

wb = openpyxl.load_workbook("contexto/dados/Captacao_Liquida.xlsx", data_only=True)
for ws in wb.worksheets:
    print("SHEET:", ws.title, ws.dimensions)
    for row in ws.iter_rows(min_row=1, max_row=3, values_only=True):
        print(row)
    print("...")

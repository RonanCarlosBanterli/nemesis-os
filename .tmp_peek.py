import openpyxl
wb = openpyxl.load_workbook('contexto/dados/Cadastro_Assessor.xlsx', read_only=True, data_only=True)
for ws in wb.worksheets:
    print('SHEET:', ws.title)
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        print(row)
        if i > 5:
            break

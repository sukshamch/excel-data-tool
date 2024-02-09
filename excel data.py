import openpyxl

file_path = "C:/Users/HPJMU/Documents/suksham011.xlsx"

try:
    wb = openpyxl.load_workbook(file_path)

    sheet = wb.active

    for row in sheet.iter_rows(values_only=True):
        print(row)

    wb.close()

except FileNotFoundError:
    print("File not found at the specified path:", file_path)
except PermissionError:
    print("Permission denied to access the file:", file_path)
except Exception as e:
    print("An error occurred:", e)

print("Hello World!!!")

import openpyxl as px



with open("out1.txt", "r") as file:
     lines = [line.rstrip().split(" ") for line in file.readlines()]
     file.close()

wb = px.Workbook()
ws = wb.active

for i in range(len(lines[0])):
    for j in range(len(lines)):
        ws.cell(row = j + 2, column = i + 2).value = str(lines[j][i])

wb.save("data.xlsx")
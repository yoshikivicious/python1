print("Hello World!!!")

import openpyxl as px

#ファイルを開く
path = 'outp.txt'
file = open(path)

#すべての行をリストとして読み込み
lines = file.readlines()

#ファイルを閉じる
file.close()

#ブックを新規作成。Workbookの'w'は必ず大文字。
wb = px.Workbook()

#出力ファイル名を指定
filename = "result.xlsx"

#アクティブなシートを取得
ws = wb.active


#listを取得するための変数
l = 1

#セルへの書き込み
i = 3
j = 5
blank = lines[l].split()
ws.cell(row=j, column=i).value = int(blank)
l += 1

#ブックを保存する
wb.save(filename)
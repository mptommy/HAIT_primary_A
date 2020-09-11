import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

# (1) Google Spread Sheetsにアクセス
def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    return worksheet

# ここでjsonfile名とkeyを入力
jsonf = "hait-primary-a-7416c5c3bb75.json"
spread_sheet_key = "1I8tP-AuB4OkIzoGBVLQKueBjVoF_B0pmw96LicwR5PU"
ws = connect_gspread(jsonf,spread_sheet_key)

def gsupdate(dic):
    #辞書を2次元配列にする
    array = [[i, v] for i, v in dic.items()]
    #スプレッドシートに書き込み
    ws.append_rows(array)
    
#sample
#dicc = [['word','単語'],['unk','うんこ']]
#ws.append_rows(dicc)




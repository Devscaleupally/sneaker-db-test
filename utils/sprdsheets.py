import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets",
     "https://www.googleapis.com/auth/drive.file", 
     "https://www.googleapis.com/auth/drive"
     ]

cred = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
client = gspread.authorize(cred)

def upload_data(data, sheet, mail=None, notify=print):
    try:
        spd = client.open(sheet)
    except:
        spd = client.create(sheet)
        spd.sheet1.append_row(["Title", "Thumbnail", "Brand", "Colorway", "Price (in USD)", "Style", "Description"])
        spd.share(mail, perm_type='anyone', role='writer')
    spd.sheet1.append_rows(data)
    return {
        'sheetTitle': spd.title,
        'sheetURL': spd.url,
    }

def export(sheet, file):
    try:
        sht = client.open(sheet).sheet1
    except Exception as e:
        print(e)
        print(e.args)
        return False
    dt = sht.get_all_values()
    dtb = [['"'+g.replace('"', '""')+'"' if ',' in g else g for g in m] for m in dt]
    with open(file, 'wb+') as fl:
        fl.write('\n'.join([','.join(it) for it in dtb]).encode())
    return True
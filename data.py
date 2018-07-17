import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('nosql.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/1TNzLOvYH-bvDmQjaORRmyFth1dlLdMFHWrMlXMsgU3k/edit?usp=drive_web&ouid=111562957143055378670').sheet1

def searchsheet(st):
   r = []
   values_list = wks.col_values(1)
   for pn in values_list:
      if st in str(pn):
        r.append(wks.row_values(wks.find(pn).row))
   if len(r) == 0:
      return('Produkt is not in Database')
   else:
      return(r)

# from twilio.rest import Client
# from pathlib import Path

# # account_sid = 'AC0959a3985e7908d6873f86f135b8b870'
# # auth_token = '[AuthToken]'
# # client = Client(account_sid, auth_token)

# # message = client.messages.create(
# # from_='+15076367863',
# # body='test',
# # to='+886988798615'
# # )

# # print(message.sid)

# #引述傳入指向位置
# p=Path('./Desktop')

# #沒傳影術，開python的位置
# p=Path()

# #resolve 找出絕對路徑
# p.resolve()

# print(p.resolve())

#引進pygsheet套件
import pygsheets

#設定google cloud 用戶：讓google sheets知道你的身份
gc=pygsheets.authorize(service_file='/Users/scofield/Documents/Python_2023Spring/class7/mythical-bazaar-384601-aa22a7fcc316.json')
#連接試算表
sht= gc.open_by_url('https://docs.google.com/spreadsheets/d/1Jtzc6dITHX6DL7Jfc-uXePtLJhLl9GvdYOjDeJos0dQ/edit#gid=0')

#利用index選取
ws=sht[0]

#選取名字
# ws=sht.worksheet_by_title('工作表1')

# ws.update_value('A1','test')


# #讀取
# value=ws.get_value('A1')
# print("A1's"+value)
# A1=ws.cell('A1')
# A1=ws.cell('A1'+A1.value)

# #刪除所有
# ws.clear()


# ws=sht[0]


# ws=sht.worksheet_by_title('工作表1')

# ws.update_value('A1','Name')

# ws.update_value('B1','Age')

# ws.update_value('A2','Amy')

# ws.update_value('B2','18')

# ws.update_value('A3','Peter')

# ws.update_value('B3','15')


# import pandas as pd

# df=pd.DataFrame(ws.get_all_records())


# print(df)


# #dataframe to worksheet
# ws.set_dataframe(df,'A1')

# import requests

# #不待條件
# r=requests.get('https://www.apple.com/tw/')
# #有條件
# payload={'key1':'value1','key2':'value2'}
# r=requests.get('https://www.apple.com/tw/',params=payload)

# r=requests.post('https://www.apple.com/tw/',data={'key':'value'})

# #列印文字
# print(r.text)
# print(r.encoding)#列出編碼
# print(r.status_code)#列http
# print(r.headers)#映出Header
# print(r.headers['Content-Type'])#映出Header
# # print(r.json())#取得json


import requests

url='https://api.exchangerate-api.com/v4/latest/TWD'

res=requests.get(url)

data=res.json()

print('日幣兌台幣的匯率為'+str(data['rates']['JPY']))
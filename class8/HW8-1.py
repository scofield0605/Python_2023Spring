import pygsheets
import requests

#設定google cloud 用戶：讓google sheets知道你的身份
gc=pygsheets.authorize(service_file='/Users/scofield/Documents/Python_2023Spring/class7/mythical-bazaar-384601-aa22a7fcc316.json')
#連接試算表
sht= gc.open_by_url('https://docs.google.com/spreadsheets/d/1Jtzc6dITHX6DL7Jfc-uXePtLJhLl9GvdYOjDeJos0dQ/edit#gid=0')
url='https://api.exchangerate-api.com/v4/latest/TWD'

#利用index選取
ws=sht[0]

res=requests.get(url)

data=res.json()

ws.update_value('A1','國家')

ws.update_value('B1','匯率')

ws.update_value('A2','日本')

ws.update_value('B2',str(data['rates']['JPY']))

ws.update_value('A3','美國')

ws.update_value('B3',str(data['rates']['USD']))

ws.update_value('A4','香港')

ws.update_value('B4',str(data['rates']['HKD']))







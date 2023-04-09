from twilio.rest import Client
from pathlib import Path

# account_sid = 'AC0959a3985e7908d6873f86f135b8b870'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
# from_='+15076367863',
# body='test',
# to='+886988798615'
# )

# print(message.sid)

#引述傳入指向位置
p=Path('./Desktop')

#沒傳影術，開python的位置
p=Path()

#resolve 找出絕對路徑
p.resolve()

print(p.resolve())


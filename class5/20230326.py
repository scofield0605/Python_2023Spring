from email.mime.image import MIMEImage
#引入MUltipart
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from email.mime.text import MIMEText
#Python專案中的電子郵件內容完成後，接下來就要設定Gmail的SMTP伺服器來寄送
import smtplib
#如果想要在電子郵件中加人圖片，則需在Python專案中引用MIMEImage類別，並且引用pathlib函式庫來讀取圖片
text=MIMEText('hello 我是python建立的信件!')

image=MIMEImage(Path('/Users/scofield/Documents/Python_2023Spring/giganigga.jpg').read_bytes())
content=MIMEMultipart()
content['subject']='2023 Pthon App 春季班DEmo'
content['from']='scofieldtsai@gmail.com'
content['to']='che3ri27@gmail.com'

content.attach(text)
content.attach(image)

smtp=smtplib.SMTP(host='smtp.gmail.com', port='587')

f=open('class5/password.txt','r')
mailToken=f.read()
f.close()

#利用 with 來自動釋放資源
with open('class5/password.txt','r')  as f:
    mailToken=f.read()


with smtp:#利用 with 來白動釋放資源
    try:
        smtp.ehlo() #驗證SMTP伺服器
        smtp.starttls() #建立加密傳輸
        smtp.login("scofieldtsai@gmail.com", mailToken)
        smtp.send_message ( content) #寄送郵件
        print ("Email is Sended completely!")
        smtp.quit ()
    except Exception as e:
        print ("Error message: ", e)






















# wuienlixmzogxazn
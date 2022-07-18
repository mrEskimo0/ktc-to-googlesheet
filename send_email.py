import smtplib
from config import EMAIL, PASSWORD


smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

smtp_object.login(EMAIL,PASSWORD)

from_address = EMAIL
to_address = EMAIL
subject = 'KTC to Google Sheet Scrape Failed'
message = 'something went wrong with the scrape'
msg = 'Subject: '+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()

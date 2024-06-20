import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
server.starttls()
sender=''  #write email id of sender
receiver='' #write email of receiver
#get your app password of gmail 
password='***************'
server.login(sender,password)
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(6)])
msg='Hello, Your OTP is '+str(otp)
#send
server.sendmail(sender,receiver,msg)
server.quit()
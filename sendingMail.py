''''This is a row program to send a mail using voice assitant.this is for understanding purpose only.'''
import smtplib

def  sendEmail(senderId,password,recieverId, content):
    '''This function is for send e-mail to any person using smtplib module.'''
    server=smtplib.SMTP('smtp.gmail.com', 587)
    # here we are using gmail SMTP(Simple Mail Transfer Protocol) server port number is 587.
    server.ehlo()
    server.starttls()
    server.login(senderId,password)      
    server.sendmail(senderId,recieverId,content)
    server.close()

query = input()
if 'send email to ' in query:
            try:
                speak("tell me your email id from which you want to send mail.")
                senderId = takeCommand()
                speak("enter your password please.")
                password = input('enter your password please::')
                speak("Tell me to whome you want to send the mail.")
                recieverId = takeCommand()
                speak("What message you want to send?")
                content=takeCommand()
                sendEmail(senderId,password,recieverId,content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry Sir im not able to send this Email currently")
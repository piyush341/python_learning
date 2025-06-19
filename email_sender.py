import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    ##reciver mail
    reciver_mail= input("enter the recevier mail: ")
    ##mail  credential
    sender_mail="onepiecesunny2001@gmail.com"
    password="rbgm vabp hzte jjuf"
    #sign in
    server.login(sender_mail,password)
    #sending mail
    subject=input("enter the subject:")
    body=input("enterthe body:")
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_mail,reciver_mail,message)
    print("mail send sucessfully")
    server.quit()
except Exception as e:
    print("an error occured",e)
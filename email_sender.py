#importing libraries
import smtplib, ssl

def sendin_email():

    port =465  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = input("Enter your email and then press enter : ")  # Enter your address
    receiver_email = input("Enter reciever email : ") # Enter receiver address
    password = input("Type your password and press enter: ")
    message = input("Type your message here\n : ")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() 
            server.starttls(context=context) # Secure the connection
            server.ehlo() 
            server.login(sender_email, password)
        except:
            print("couldnot login or send email")
sendin_email()
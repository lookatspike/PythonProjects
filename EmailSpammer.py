import smtplib as sp #importing smtp library

email_mittente = ""
password_mittente = ""
destinatario = ""
oggetto = "Subject: Ciao a tutti \n\n"
contenuto = "@marco.dev"
numero_email = 10
messaggio = oggetto + contenuto

server = sp.SMTP('smtp.gmail.com:587') #Creating SMTP server with Gmail 
server.ehlo() #Starting Private Tunnel For connection
server.starttls() #Starting Connection 
server.login(email_mittente, password_mittente) #Login

for i in range(1, numero_email): #loop
    server.sendmail(email_mittente, destinatario, messaggio) #sending mail
    print(f"Email inviate: {i}")
server.quit() #Closing Server
import smtplib
import getpass

username = raw_input("Username: ")
passwd = getpass.getpass("Password: ")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, passwd)
msg = raw_input("Message to send: ")
send_to = raw_input("Recipient mail: ")
server.sendmail(username, send_to, msg)
server.quit()

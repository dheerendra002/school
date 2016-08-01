import smtplib
import getpass

send_to = raw_input("Recipient mail: ")
msg = raw_input("Message to send: ")
username = raw_input("Email: ")
passwd = getpass.getpass("Password: ")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, passwd)
server.sendmail(username, send_to, msg)
server.quit()

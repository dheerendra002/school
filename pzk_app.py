import smtplib
import getpass
from scrape import scrape

msg = scrape.get_data_status()
send_to = raw_input("Recipient mail: ")
username = "micscov2@gmail.com"
passwd = getpass.getpass("Password: ")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, passwd)
server.sendmail(username, send_to, msg)
server.quit()

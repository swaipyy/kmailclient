import smtplib, os,  stdiomask, getpass, sys
from email.message import EmailMessage
from socket import gaierror
import banner

class KmaiClient(object):
    def __init__(self):
        self.smtps = {"1":"smtp.gmail.com:587",
                      "2":"mail.cock.li:587",
                      "3":"smtp.office365.com:587",
                      "4":"smtp.live.com:25",
                      "5":"smtp.mail.yahoo.com:587"}

    def main(self):
        os.system("cls")
        banner.opciones()

        opcion = input(">> ")
        smtp = self.smtps[opcion].split(":")[0]
        puerto = self.smtps[opcion].split(":")[1]

        login_input = input(f"[*] [{smtp}] Enter your Email: ")
        password = stdiomask.getpass(prompt='[*] Enter your password: ', mask ='*')

        if self.tester(smtp, puerto, login_input, password) == True:
            print(f"[+] Login successful {smtp}")
            mensajito = input("[*] Send message [y/n]: ")
            if mensajito == "y":
                os.system("cls")
                self.send(smtp, puerto, login_input, password)
            if mensajito == "n":
                sys.exit(1)
        else:
            print(self.tester(smtp, puerto, login_input, password))


    def send(self, smtp, puerto, login_input, password):
        receiver = input("[*] Enter the receiver: ")
        subject = input("[*] Enter the subject: ")
        message = input("[*] Enter your message: ")

        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = login_input
        msg['To'] = receiver

        try:
            with smtplib.SMTP(smtp, puerto) as server:
                server.starttls()
                print("Server start")
                server.login(login_input, password)
                print("Login account successful")
                server.send_message(msg)
                print("Mail sended successful")
                server.quit()
                return True

        except (gaierror, ConnectionRefusedError):
            return "[!] Failed to connect to the server, Bad connection settings."


        except smtplib.SMTPServerDisconnected:
            return '[!] Failed to connect to the server. Wrong user/password?'

        except smtplib.SMTPException as e:
            return '[!] SMTP error occurred: ' + str(e)

    def tester(self, smtp, puerto, login_input, password):
        try:
            with smtplib.SMTP(smtp, puerto) as server:
                server.starttls()
                server.login(login_input, password)
                server.quit()
                return True

        except smtplib.SMTPServerDisconnected:
            return "Failed to connect to the server. Wrong Email/password?"

        except smtplib.SMTPAuthenticationError:
            return "Failed to authenticacion. Wrong Email/Password?"

        except (gaierror, ConnectionRefusedError):
            return "Bad connection settings, please insert a valid mail service."


if __name__ == '__main__':
    while True:
        banner.inicio()
        option = input("Enter a command please: ")
        client = KmaiClient()
        try:
            if option == "1":
                client.main()
        except KeyError:
            print("[!] No existe esa opcion")

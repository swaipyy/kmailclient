import smtplib, os,  stdiomask, getpass
from colorama import Fore, Style
from email.message import EmailMessage
from socket import gaierror

os.system("clear")
print('if u need help just type "?" ')
getpass.getpass("Press ENTER")
os.system('clear')

kmail_client =     '''
     _   __                _ _        _ _            _
    | | / /               (_) |      | (_)          | |
    | |/ / _ __ ___   __ _ _| |   ___| |_  ___ _ __ | |_
    |    \| '_ ` _ \ / _` | | |  / __| | |/ _ \ '_ \| __|
    | |\  \ | | | | | (_| | | | | (__| | |  __/ | | | |_
    \_| \_/_| |_| |_|\__,_|_|_|  \___|_|_|\___|_| |_|\__|'''

while True:

    os.system('clear')

    print(kmail_client)

    option = input("Enter a command please: ")

    #Start login
    if option == "login":
        #Login
        while True:

            os.system("clear")
            print(kmail_client)

            while True:
                print("Type 'help' to see a list of default mail service")
                mail_service_input = input("Enter your mail service: ")
                if mail_service_input in ("help", "gmail", "cock.li", "outlook", "hotmail", "yahoo", "custom"):
                    if mail_service_input == "help":
                        print('''
The defaults mail service are:
gmail
cock.li
outlook
hotmail
yahoo
And for other service type custom
                              ''')
                    elif mail_service_input == "gmail":
                        mail_service = "smtp.gmail.com"
                        port = 587
                        break
                    elif mail_service_input == "cock.li":
                        mail_service = "mail.cock.li"
                        port = 587
                        break
                    elif mail_service_input == "outlook":
                        mail_service = "smtp.office365.com"
                        port = 587
                        break
                    elif mail_service_input == "hotmail":
                        mail_service = "smtp.live.com"
                        port = 25
                        break
                    elif mail_service_input == "yahoo":
                        mail_service = "smtp.mail.yahoo.com"
                        port = 587
                        break
                    elif mail_service_input == "custom":
                        while True:
                            mail_service = input("Enter your mail service: ")
                            port = input("Enter the port (Usually is 587): ")
                            try:
                                with smtplib.SMTP(mail_service, port) as server:
                                    server.starttls()
                                    print(Fore.CYAN + "Your mail service is compatible with smtp!" + Style.RESET_ALL)
                                    server.quit()
                                    break
                            except (gaierror, ConnectionRefusedError):
                                print("Bad connection settings, please insert a valid mail service.")
                                getpass.getpass("Press enter...")
                        break

            login_input = input("Enter your Email: ")
            password = stdiomask.getpass(prompt='Enter your password: ', mask ='*')

            try:
                with smtplib.SMTP(mail_service, port) as server:
                    server.starttls()
                    server.login(login_input, password)
                    print(Fore.CYAN + "Login successful" + Style.RESET_ALL)
                    getpass.getpass("Press enter...")
                    server.quit()
                    break
            except smtplib.SMTPServerDisconnected:
                print("Failed to connect to the server. Wrong Email/password?")
                getpass.getpass("Press enter...")
            except smtplib.SMTPAuthenticationError:
                print("Failed to authenticacion. Wrong Email/Password?")
                getpass.getpass("Press enter...")
            except (gaierror, ConnectionRefusedError):
                print("Bad connection settings, please insert a valid mail service.")
                getpass.getpass("Press enter...")


        os.system("clear")
    #End login

    #Start send
    elif option == "send":
        
        print(Style.RESET_ALL)
        os.system("clear")

        print(kmail_client)

        receiver = input("Enter the receiver: ")
        subject = input("Enter the subject: ")
        message = input("Enter your message: ")

        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = login_input
        msg['To'] = receiver

        try:

            with smtplib.SMTP(mail_service, 587) as server:
                server.starttls()
                print( Fore.CYAN + "Server start" + Style.RESET_ALL)
                server.login(login_input, password)
                print( Fore.CYAN + "Login account successful" + Style.RESET_ALL)
                server.send_message(msg)
                print( Fore.GREEN + "Mail sended successful" + Style.RESET_ALL)
                server.quit()
                getpass.getpass("PRESS ENTER TO CONTINUE...")

        except (gaierror, ConnectionRefusedError):
            print("Failed to connect to the server, Bad connection settings.")
            getpass.getpass("PRESS ENTER TO CONTINUE...")

        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
            getpass.getpass("PRESS ENTER TO CONTINUE...")

        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
            getpass.getpass("PRESS ENTER TO CONTINUE...")

            os.system("clear")
    #End of send

    #Start help
    elif option == "?":
        print("The command's are: 'login', 'send', 'exit' ")
        getpass.getpass('Press ENTER')
    #End help

    #Start exit
    elif option == "exit":
        break
    #End exit

    #Start invalid command
    else:
        print('please insert a valid command')
        getpass.getpass('Press ENTER')
    #End invalid command

print(Style.RESET_ALL)
os.system("clear")

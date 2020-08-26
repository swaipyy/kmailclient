import smtplib, os,  stdiomask
from colorama import Fore, Style
from email.message import EmailMessage
from socket import gaierror

#Send mail function
def send_mail(login, password, kmail_client, mail_service):

    print(Style.RESET_ALL)
    os.system("clear")

    print(kmail_client)

    receiver = input("Enter the receiver: ")
    subject = input("Enter the subject: ")
    message = input("Enter your message: ")

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = login
    msg['To'] = receiver

    try:

        with smtplib.SMTP(mail_service, 587) as server:
            server.starttls()
            print( Fore.BLUE + "Server start" + Style.RESET_ALL)
            server.login(login, password)
            print( Fore.BLUE + "Login account successful" + Style.RESET_ALL)
            server.send_message(msg)
            print( Fore.GREEN + "Mail sended successful" + Style.RESET_ALL)
            server.quit()
            input("PRESS ENTER TO CONTINUE...")

    except (gaierror, ConnectionRefusedError):
        print("Failed to connect to the server, Bad connection settings.")
        input("PRESS ENTER TO CONTINUE...")

    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')
        input("PRESS ENTER TO CONTINUE...")

    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
        input("PRESS ENTER TO CONTINUE...")
###end of the function

os.system("cls")
print('if u need help just type "?" ')
input("Press ENTER")
os.system('cls')

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

    if option == "login":
        mail_service = input("Enter the mail service: ")
        login_input = input("Enter your mail: ")
        password = stdiomask.getpass(prompt='Enter your password: ', mask ='*')
        os.system("clear")

    elif option == "send":
        login = login_input
        server.send_mail(login, password, kmail_client, mail_service)
        os.system("clear")

    elif option == "?":
        print("The command's are: 'login', 'send', 'exit' ")
        input('Press ENTER')

    elif option == "exit":
        break

    else:
        print('please insert a valid command')
        input('Press ENTER')


print(Style.RESET_ALL)
os.system("clear")

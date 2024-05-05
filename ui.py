from service import login
from utils import ResponseData
from colorama import Fore


def print_response(response: ResponseData):
    color = Fore.GREEN if response.status else Fore.RED
    print(color + str(response.data) + Fore.RESET)


def menu():
    print('Login => 1')
    print('Register => 2')
    print('Logout => 3')
    print('Quit => q')
    return input('?: ')


def authentication():
    username = input('Username: ')
    password = input('Password: ')
    response: ResponseData = login(username, password)
    print_response(response)
def logout():
    print("Successfully logged out.")


def login_menu():
    print('Username: ')
    username = input()
    print('Password: ')
    password = input()
    return username, password

def login():
    username, password = login_menu()
    response: ResponseData = login(username, password)
    print_response(response)

def register_menu():
    print('Enter your desired username: ')
    username = input()
    print('Enter your password: ')
    password = input()
    return username, password

def register():
    username, password = register_menu()
    response: ResponseData = register(username, password) 
    print_response(response)

if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            logout()
        elif choice == 'q':
            break




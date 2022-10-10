import sys
from dbhelper import DBhelper

class FlipKart:

    def __init__(self):
        #create connection to the database here:
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input('''
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        ''')
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("Enter your name:")
        email = input("Enter the email:")
        password = input("Enter your mail password:")

        response = self.db.register(name,email,password)
        if response:
            print("Registration Successful!")
        else:
            print("Registration failed")
        self.menu()

obj=FlipKart()
import sys
from dbhelper import DBhelper

class Flipkart:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to Login 
        2. Enter 2 to Register
        3. Enter 3 to Exit from app
        """)
        if user_input == '1':
            self.login()
        elif user_input == '2':
            self.register()
        else:
            self.logout()

    def logout(self):
        self.db.close_connection()
        print("By by!")
        sys.exit()

    def login_menu(self, email, password):
        user_input = input("""
        1. Enter 1 to See Profile
        2. Enter 2 to Edit Profile
        3. Enter 3 to Delete Account
        4. Enter 4 to Logout
        """)

        if user_input == '1':
            self.see_profile(email, password)
        elif user_input == '2':
            self.edit_profile(email)
        elif user_input == '3':
            self.delete_account(email, password)
        elif user_input == '4':
            self.logout()

    def see_profile(self, email, password):
        response = self.db.see_profile(email)
        if response:
            print(f"Name is {response[0][1]}, Email is {response[0][2]} and Password is {response[0][3]}")
            self.login_menu(email, password)
        else:
            print("Profile not found.")
            self.see_profile(email, password)

    def edit_profile(self, email):
        update_name = input("Enter Name: ")
        update_email = input("Enter Email: ")
        update_password = input("Enter Password: ")
        success = self.db.edit_profile(email, update_name, update_email, update_password)
        if success:
            print("Profile updated successfully.")
            self.login()
        else:
            print("Failed to update profile. Please try again.")
            self.edit_profile(email)

    def delete_account(self, email, password):
        success = self.db.delete_account(email, password)
        if success:
            print("Account deleted successfully.")
            self.menu()
        else:
            print("Failed to delete account.")
            self.delete_account(email, password)

    def register(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        success = self.db.register(name, email, password)
        if success:
            print("Registration Successful. Please login!")
            self.login()
        else:
            print("Registration failed. Please try again.")
            self.register()

    def login(self):
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        response = self.db.login(email, password)
        if response:
            print(f"Welcome back! {response[0][1]}")
            self.login_menu(response[0][2], response[0][3])
        else:
            print("Invalid email or password.")
            self.login()

obj = Flipkart()
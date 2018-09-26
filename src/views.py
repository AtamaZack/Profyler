# Dependecies
from .models import DbModel, UserModel
DB = DbModel()

def sign_up_form(input_tuple):
    user_obj = UserModel(input_tuple)
    DB.add_obj(user_obj, 'users')
def login_form(input_tuple):
	pass
def view_profile():
    return (DB.user_table[-1]).display_details()

def user_method_selector(option):
    if option == 1:
        name = input('enter your name: ')
        username = input('enter a username: ')
        age = input('enter your age: ')
        email = input('enter your email: ')
        password = input('enter a password: ')
        gender = input('enter your gender (M/F): ')
        input_tuple = (name, username, age, email, password, gender)
        if sign_up_form(input_tuple):                    
            print("----------- OUTPUT RESULT -----------")
            print("Registration successful!")
            print("-------------------------------------")            
    if option == 2:
        pass
def function_method_selector(option):
    if option == 1:                    
        print("----------- OUTPUT RESULT -----------")
        print(view_profile())
        print("-------------------------------------")

	
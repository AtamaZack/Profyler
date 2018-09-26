# Dependecies
from src.views import user_method_selector, function_method_selector

# App user options
USER_OPTIONS = '------User options------\n1. Sign up\n2. Login\n3. Exit application'
# App logged in function options
FUNCTION_OPTIONS = '------Function options------\n1. View profile\n2. Edit fields\n3. Logout'
# User property edit options
EDIT_OPTIONS = '------Function options------\n1. Password\n2. Email\n3. Back'
# App exit status
EXIT_STATUS = False
EXIT_FUNCTION = False
EXIT_EDIT = False
def invalid_input():
    print("----------- OUTPUT RESULT -----------")
    print('invalid option\nhint: input must be a digit')
    print("-------------------------------------")

if __name__ == "__main__":
    while not EXIT_STATUS:
        print(USER_OPTIONS)
        USER_OPTION = input('select a user option: ')
        if USER_OPTION.isdigit():
            USER_OPTION = int(USER_OPTION)
            if USER_OPTION <= 2:
                if user_method_selector(USER_OPTION) == 'error':                    
                    print("----------- OUTPUT RESULT -----------")
                    print("invalid function option\nhint: 1, 2 and 3")
                    print("-------------------------------------")
                else:
                    while not EXIT_FUNCTION:
                        print(FUNCTION_OPTIONS)
                        FUNTCION_OPTION = input('select a function option: ')
                        if FUNTCION_OPTION.isdigit():
                            FUNTCION_OPTION = int(FUNTCION_OPTION)
                            if FUNTCION_OPTION <= 2:
                                if function_method_selector(FUNTCION_OPTION) == 'error':
                                    pass
                                else:
                                    pass
                            elif FUNTCION_OPTION == 3:
                                EXIT_FUNCTION = True
                            else:
                                print("----------- OUTPUT RESULT -----------")
                                print('invalid function option\nhint: only 1, 2 and 3')
                                print("-------------------------------------")
                        else:
                            invalid_input()
            elif USER_OPTION == 3:
                print("----------- OUTPUT RESULT -----------")
                print("Thank you for using Profyler")
                print("-------------------------------------")
                EXIT_STATUS = True
            else:
                print("----------- OUTPUT RESULT -----------")
                print('invalid user option\nhint: only 1, 2 and 3')
                print("-------------------------------------")
        else:
            invalid_input()

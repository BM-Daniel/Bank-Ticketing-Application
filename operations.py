from datetime import datetime
from string import punctuation

def get_user():
    """
    Returns the type of user
    :return: user
    """

    # Validates the user's input
    while True:
        print("User Categories:")
        print("\t1. Admin")
        print("\t2. Customer")
        print("\t3. Teller")
        user = input("Enter the type of user: ")

        if user.title().strip() == "Admin" or user == "1":
            return 1  # Returns 1 for Admin
        elif user.title().strip() == "Customer" or user == "2":
            return 2  # Returns 2 for Customer
        elif user.title().strip() == "Teller" or user == "3":
            return 3  # Returns 3 for Teller
        else:
            print("\nEnter a valid option!!!\n")  # Displays error message


def get_service():
    """
    Returns the type of service
    :return: service
    """
    # Validates the user's input
    while True:
        print("Services:")
        print("\t1. Deposit")
        print("\t2. Withdrawal")
        print("\t3. Transfer")
        service_request = input("Select a service: ")

        if service_request.title().strip() == "Deposit" or service_request == "1":
            return "Deposit"
        elif service_request.title().strip() == "Withdrawal"  or service_request == "2":
            return "Withdrawal"
        elif service_request.title().strip() == "Transfer" or service_request == "3" :
            return "Transfer"
        else:
            print("\nEnter a valid option!!!\n")  # Displays error message


def get_admin_task():
    """
    Returns the task of admin
    :return: task
    """
    # Validates admin input
    print("\nWelcome Admin!")
    input("Enter password: ")
    while True:
        try:
            print("\nTasks: ")
            print("\t1. Create a teller queue")
            print("\t2. Reassign active teller")
            task = int(input("Enter task: "))

            if task < 1 or task > 2:
                print("\nEnter a valid option!")
            else:
                return task
        except ValueError:
            print("\nEnter a valid option!")

def get_teller_choice():
    while True:
        try:
            print("\t1. Serve Queue")
            print("\t2. View Queue")
            print("\t3. Log out")
            choice = int(input("Enter choice: "))

            if choice < 1 or choice > 3:
                print("\nEnter a correct choice\n")
            else:
                return choice
        except ValueError:
            print("\nEnter a valid number\n")

def validate_teller(teller_list):
    while True:
        print("\nPlease enter the following details: ")
        teller_id = input("Teller id: ")
        print("Enter service type: ")
        service_request = get_service()
        print()

        for i in range(len(teller_list)):
            if teller_id == teller_list[i].teller_ID and service_request == teller_list[i].service:
                return i

        print("Incorrect Details!!!")

## UNIQUE ID GENERATOR
def make_account_id(prefix='DT-'):
    '''Random manipulation to generate id from date and time'''
    code = str(datetime.today())
    for l in code:
        if l in punctuation:
            code = code.replace(l,'')
    code = code.split()
    code = str(int(code[0])+int(code[1])//100)
    return prefix + code[:3] + '-' + code[3:6]
# ## INPUT FUNCTIONS
# def get_name():
#     '''reads user name input, checks validity and returns the valid name.'''
#
#     name = input("BT>> ").strip().capitalize()
#     # check if is name is all letters and hiphens
#     while not ('-'  in name or name.isalpha() or '' in name):
#         print("Name should be made of letters only\nTry again...\n")
#         name = input("BT>> ").capitalize()
#     return  name
#
# def get_amount():
#     '''Reads user amount input, checks validity and returns the valid amount.
#        Checks if input IS DIGIT and allows FOR DECIMAL
#     '''
#     amount = input("BT>> ")
#
#     # check if amount is all numbers
#     while not ('.' in amount or amount.isdigit()):
#         print("Amount should be numbers only\nTry again...\n")
#         amount = input("BT>> ")
#     return  round(float(amount),2)
#
# def get_fullname():
#     '''Returns a fullname in a list'''
#     print("BT>> Enter first name")
#     first_name = get_name()
#
#     print("BT>> Enter surname")
#     surname = get_name()
#
#     print("BT>> Enter other name or leave blank")
#     other_name = get_name()
#     return [first_name, surname, other_name]
#
# def select_cartegory(options):
#     '''allows user to select cartegory of service and returns service.
#        Checks if choice is INTEGER and if choise is IN RANGE.
#     '''
#     cart_service = options
#     selection = -1
#     print("BT>> Select a choice")
#     for k,v in options.items():
#         print(f'{k} --> {v}')
#
#     while True:
#         try:
#             selection = int(input("BT>> Select a number: "))
#             if selection in range(1,len(cart_service.keys())+1):
#                 return options[str(selection)]
#             else:
#                 print("Choice out of range\n")
#         except ValueError:
#             print("Input should be an integer\n")
#             continue

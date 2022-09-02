from datetime import datetime
from string import punctuation


## INPUT FUNCTIONS
def get_name():
    '''reads user name input, checks validity and returns the valid name.'''
    
    name = input("BT>> ").strip().capitalize()
    # check if is name is all letters and hiphens
    while not ('-'  in name or name.isalpha() or '' in name):
        print("Name should be made of letters only\nTry again...\n")
        name = input("BT>> ").capitalize()
    return  name

def get_amount():
    '''Reads user amount input, checks validity and returns the valid amount.
       Checks if input IS DIGIT and allows FOR DECIMAL
    '''
    amount = input("BT>> ")

    # check if amount is all numbers
    while not ('.' in amount or amount.isdigit()):
        print("Amount should be numbers only\nTry again...\n")
        amount = input("BT>> ")
    return  round(float(amount),2)

def get_fullname():
    '''Returns a fullname in a list'''
    print("BT>> Enter first name")
    first_name = get_name()

    print("BT>> Enter surname")
    surname = get_name()

    print("BT>> Enter other name or leave blank")
    other_name = get_name()
    return [first_name, surname, other_name]

def select_cartegory(options):
    '''allows user to select cartegory of service and returns service.
       Checks if choice is INTEGER and if choise is IN RANGE.
    '''
    cart_service = options
    selection = -1
    print("BT>> Select a choice")
    for k,v in options.items():
        print(f'{k} --> {v}')
    
    while True:
        try:
            selection = int(input("BT>> Select a number: "))
            if selection in range(1,len(cart_service.keys())+1):
                return options[str(selection)]
            else:
                print("Choice out of range\n")
        except ValueError:
            print("Input should be an integer\n")
            continue

## UNIQUE ID GENERATOR
def make_account_id(prefix='DT-'):
    '''Random manipulation to generate id from date and time'''
    code = str(datetime.today())
    for l in code:
        if l in punctuation:
            code = code.replace(l,'')
    code = code.split()
    code = str(int(code[0])+int(code[1])//100)
    return prefix + code[:4] + '-' + code[4:]
from operations import make_account_id
from datetime import datetime

## ACCOUNT OBJECT
class Account:
    def __init__(self, account_name, account_type=None):
        self.name = account_name
        self.type = account_type
        self.balance = 0
        self.id = make_account_id()

    def check_balance(self):
        return self.balance 
    
    def export_data(self,):
        '''collects useful data and metadata into a dictionary'''
        account_db = {}
        account_db['Account Name'] = self.name
        account_db['Account Number']= self.id
        account_db['Account Type']= self.type
        account_db['Account Balance']= self.check_balance()
        account_db['__DATE CREATED']= str(datetime.today())
        return account_db

    def __repr__(self):
        firstname,surname,other_name = 0,1,2
        return f'''
            Account Name: {self.name[surname]}, {self.name[firstname]} {self.name[other_name]}
            Account Number: {self.id}
            Account Type: {self.type} Account
            Account Balance: *** 
        '''


## ACCOUNT SERVICES FUNCTIONS
def withdraw(amount, account, notify=True):
    balance = account.balance
    if balance and (balance - amount) > 0:
        balance = balance - amount
    else:
        # print(f"BT<< Withdrawal of GHS {amount} failed due to insufficient balance in account no: {account.name}\n")
        notification(0,withdraw,amount,account,notify)
        return 0
    account.balance = balance
    # print(f"BT<< Withdrawal GHS {amount} successful. {account.name} balance is GHS {account.balance}\n")
    notification(1,withdraw,amount,account,notify)
    return 1

def deposit(amount,account, notify=True):
    account.balance += amount
    # print(f"BT<< Deposit of GHS {amount} successful. {account.name} balance is GHS {account.balance}\n")
    notification(1,deposit,amount,account,notify)
    return 1

def transfer(sender_account, receiver_account, amount, notify=True):
    withdraw_result = withdraw(amount,sender_account,False)
    if withdraw_result:
        receiver_account.balance += amount
    print(f"\nBT<< Transfer of GHS {amount} from {sender_account.name} to {receiver_account.name}...")
    notification(withdraw_result,transfer,amount,sender_account)

def notification(success_value,function,amount,account,notify=True):
    '''Dynamically generates notifications depending on service rendered'''
    if notify:
        prep, status = (' of','Successful') if success_value else ('','Failed to')
        print(f"BT<< {status} {function.__name__}{prep} GHS {amount}. {account.name} balance is GHS {account.balance}")

def verify_password(user, password, user_type):
    '''This is just for trials'''
    if password == 'password':
        return True
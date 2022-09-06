from Customer import Customer
from Teller import TellerQueue
from Ticketing_System import teller
from operations import *
import openpyxl, xlrd, os
from openpyxl import Workbook

teller_list = []
def create_tq(*data):
    teller_name, teller_service, teller_id = data

    if teller_service == "Deposit":
        deposit = TellerQueue(teller_id, teller_name.title(), teller_service)
        teller_list.append(deposit)  # Adds deposit queue to the teller list
    elif teller_service == "Withdrawal":
        withdrawal = TellerQueue(teller_id, teller_name.title(), teller_service)
        teller_list.append(withdrawal)  # Adds withdrawal queue to the teller list
    else:
        transfer = TellerQueue(teller_id, teller_name.title(), teller_service)
        teller_list.append(transfer)  # Adds transfer queue to the teller list

def reassign_tq(*data):
    teller_name, service, teller_id = data
    if len(teller_list) == 0:
            print("\nNo teller queues have been created\n")
            return 
    teller_absent = True

    for i in range(len(teller_list)):
        if teller_list[i].service.title() == service.title():
            new_teller_name = teller_name.title()
            teller_list[i].teller_name = new_teller_name.title()
            print(f"{new_teller_name} has been reassigned to {service} queue\n")
            teller_absent  = False

    if teller_absent:
        print("\nThe service queue does not exist!\n")


def del_tq(*data):
    teller_name = data[0]
    for i in range(len(teller_list)):
        if teller_name.title() == teller_list[i].teller_name:
            teller_list.pop(i)
            print(f"{teller_name.title()} was deleted")


def generate_id(name):
    if len(name)>=4:
        name = name[:4].lower() + "21"
    else:
        name = name+"0"*(4-len(name)) + "21"
    return name


def generate_ticket_id():
    return make_account_id()

def check_service(service):
    for tq in teller_list:
        if service == tq.service:
            return True

    return False

def create_customer(name, ticket_id, service):
    new_customer = Customer(name, service, ticket_id)

    for tq in teller_list:
        tq.enqueue(new_customer)


def validate_teller(teller_id):
    for tq in teller_list:
        if teller_id == tq.teller_ID:
            return True
    
    return False

def check_tq(teller_id):
    for tq in teller_list:
        if tq.teller_ID == teller_id:
            if not tq.is_empty():
                return True

    return False

def return_tq(teller_id):
    for tq in teller_list:
        if tq.teller_ID == teller_id:
            return tq

def number_of_customers():
    customers = 0
    for tq in teller_list:
        customers += tq.current_queue_size()
    
    return customers
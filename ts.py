from Customer import Customer
from Teller import TellerQueue
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
    teller_name, service = data
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
    return name[0][0:4].lower() + "21"
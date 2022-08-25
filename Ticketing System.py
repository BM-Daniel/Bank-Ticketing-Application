from Customer import Customer
from Teller import TellerQueue

print("*" * 6, "Welcome to DIGJES Bank", "*" * 6, end="\n")

ticket_id = 0

def get_user():
    while True:
        print("User Categories:")
        print("\t1. Admin")
        print("\t2. Customer")
        print("\t3. Teller")
        user = input("Enter the type of user: ")

        if user.title().strip() == "Admin" or user == "1":
            return 1
        elif user.title().strip() == "Customer"  or user == "2":
            return 2
        elif user.title().strip() == "Teller" or user == "3" :
            return 3
        else:
            print("\nEnter a valid option!!!\n")

def get_service_request():
    while True:
        print("Service Request:")
        print("\t1. Deposit")
        print("\t2. Withdrawal")
        print("\t3. Transfer")
        service_request = input("Select a service request: ")

        if service_request.title().strip() == "Deposit" or service_request == "1":
            return "Deposit"
        elif service_request.title().strip() == "Withdrawal"  or service_request == "2":
            return "Withdrawal"
        elif service_request.title().strip() == "Transfer" or service_request == "3" :
            return "Transfer"
        else:
            print("\nEnter a valid option!!!\n")


def get_task():
    while True:
        try:
            print("Welcome Admin!")
            print("Tasks: ")
            print("\t1. Create a teller queue")
            print("\t2. Reassign active teller")

            task = int(input("What task will you like to accomplish?"))
            if task < 1 or task > 2:
                print("\nEnter a correct task!!!\n")
            else:
                return task
        except ValueError:
            print("\nEnter a correct task!!!")


def admin():
    task = get_task()
    


def customer(ticket_id, teller_queue):
    print("Please enter the following details: ")
    customer_name = input("Name: ")
    service_request = get_service_request()
    amount = 0
    try:
        amount = round(float(input("Amount of Transaction: ")), 2)
    except ValueError:
        print("Enter a valid amount")

    priority_level = False
    if amount > 10000:
        priority_level = True

    ticket_id += 1

    customer = Customer(customer_name, service_request, ticket_id, priority_level)
    teller_queue.enqueue(customer)

    return f"Welcome {customer_name}. You have a place in the {service_request} queue." \
           f"\nYour ticket number is #{ticket_id}"








get_user()



from Customer import Customer
from Teller import TellerQueue

print("*" * 6, "Welcome to DIGESJC Bank", "*" * 6, end="\n")  # Welcomes user

ticket_id = 0
teller_id = 0


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


def get_task():
    """
    Returns the task of admin
    :return: task
    """

    # Validates admin input
    while True:
        try:
            print("Welcome Admin!")
            print("Tasks: ")
            print("\t1. Create a teller queue")
            print("\t2. Reassign active teller")
            task = int(input("What task will you like to accomplish?"))

            if task < 1 or task > 2:
                print("\nEnter a correct task!\n")
            else:
                return task
        except ValueError:
            print("\nEnter a correct task!")


def admin(teller_id, teller_list):
    """
    Allows admin to create teller queues and re-assign an active teller
    :param teller_id:
    :param teller_list:
    :return:
    """
    task = get_task()

    # Creates a new teller queue
    if task == 1:
        print("Please input teller details:")
        teller_name = input("Name: ")
        teller_service = get_service()
        teller_id += 1  # Generates a new teller id

        if teller_service == "Deposit":
            deposit = TellerQueue(teller_id, teller_name, teller_service)
            teller_list.append(deposit)  # Adds deposit queue to the teller list
        elif teller_service == "Withdrawal":
            withdrawal = TellerQueue(teller_id, teller_name, teller_service)
            teller_list.append(withdrawal)  # Adds withdrawal queue to the teller list
        else:
            transfer = TellerQueue(teller_id, teller_name, teller_service)
            teller_list.append(transfer)  # Adds transfer queue to the teller list

        return f"{teller_service} queue has been created"


def customer(ticket_id, teller_queue):
    """
    Adds a new customer to a particular teller queue
    :param ticket_id:
    :param teller_queue:
    :return: success message
    """
    print("Please enter the following details: ")
    customer_name = input("Name: ")
    service_request = get_service()
    amount = 0
    try:
        amount = round(float(input("Amount of Transaction: ")), 2)
    except ValueError:
        print("Enter a valid amount")

    priority_level = False
    if amount > 10000:
        priority_level = True

    ticket_id += 1  # Generates a new ticket id

    new_customer = Customer(customer_name.title(), service_request, ticket_id, priority_level)
    teller_queue.enqueue(new_customer)  # Adds a customer to a particular teller queue

    return f"Welcome {customer_name}. You have a place in the {service_request} queue." \
           f"\nYour ticket number is #{ticket_id}"


class TellerQueue:
    """A class for tellers"""
    front = 0 # Indicates the beginning of the queue
    rear = -1 # Indicates the end of the queue

    def __init__(self, teller_ID, teller_name, service, max_capacity=50):
        self.teller_ID = teller_ID
        self.teller_name = teller_name
        self.service = service
        self.queue = []  # Set queue to empty
        self.max_capacity = max_capacity
        self.queue_size = 0  # Set current queue size to 0
        self.priority_count = 0

    def is_empty(self):
        """Checks if queue is empty"""
        return self.queue == []

    def is_full(self):
        """Checks if queue is full"""
        return self.queue_size == self.max_capacity

    def enqueue(self, customer):
        """Adds customer to the queue"""

        if self.is_full():  # Avoids Queue Overflow
            raise Exception("Queue is full")

        if customer.service_request == self.service: # Matches customer to teller
            if customer.priority_level:
                self.push_front(customer)
            else:
                self.queue.append(customer)
            self.queue_size += 1  # Increments the current queue size

    def dequeue(self):
        """Removes customer from the queue"""

        if self.is_empty():  # Avoids Queue Underflow
            raise Exception("Queue is empty")

        self.queue_size -= 1
        customer = self.queue.pop(self.front)
        return (customer.name, customer.ticket_ID, customer.service_request)

    def current_queue_size(self):
        """Return the current number of customers in the queue"""
        return self.queue_size

    def __repr__(self):
        """Displays the customers in the queue"""
        print("Name", " " * 15, "Ticket")
        for i in range(self.current_queue_size()):
            print(f"{str(self.queue[i].name):<20} #{str(self.queue[i].ticket_ID)}")
        print(f"\nNumber of Customers: {self.current_queue_size()}")
        return ""

    def push_front(self, customer):
        self.queue.insert(self.priority_count, customer)
        self.priority_count += 1

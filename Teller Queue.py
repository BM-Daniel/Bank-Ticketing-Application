
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
            self.queue.append(customer)
            self.queue_size += 1  # Increments the current queue size

    def dequeue(self):
        """Removes customer from the queue"""

        if self.is_empty():  # Avoids Queue Underflow
            raise Exception("Queue is empty")

        self.queue_size -= 1
        return f"Ticket number {self.queue.pop(self.front).ticket_ID} has been served"

    def current_queue_size(self):
        """Return the current number of customers in the queue"""
        return self.queue_size

    def __repr__(self):
        """Displays the customers in the queue"""
        for i in range(self.current_queue_size()):
            print(f"{str(self.queue[i].name)}: {str(self.queue[i].ticket_ID)}")

        return ""
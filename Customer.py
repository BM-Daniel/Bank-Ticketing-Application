

class Customer:
    """A class for customers"""
    priority_level = False

    def __init__(self, name, service_request, ticket_ID, priority_level=False):
        self.name = name
        self.service_request = service_request
        self.ticket_ID = ticket_ID
        self.priority_level = priority_level

    def set_priority_level(self, priority_level):
        """Sets priority level of the customer"""
        self.priority_level = priority_level

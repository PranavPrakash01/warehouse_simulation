# items.py

class Item:
    def __init__(self, serial_id, name, weight, location):

        self.name = name
        self.serial_id = serial_id
        self.weight = weight
        self.location = location

    def __str__(self):

        return f"Item[Weight: {self.weight}, Location: {self.location}]"
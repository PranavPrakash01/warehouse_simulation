# items.py

class Item:
    def __init__(self, serial_id, name, weight, location):
        self.serial_id = serial_id
        self.name = name
        self.weight = weight
        self.location = location

    def info(self):
        return f"name: {self.name}, weight: {self.weight}, location: {self.location}"

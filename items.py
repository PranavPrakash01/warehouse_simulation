# items.py

class Item:
    def __init__(self, weight, location):

        self.weight = weight
        self.location = location

    def __str__(self):

        return f"Item[Weight: {self.weight}, Location: {self.location}]"
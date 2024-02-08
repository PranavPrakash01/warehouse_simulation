# conveyor.py

from items import Item

class Conveyor:
    def __init__(self, name):

        self.name = name
        self.items_on_conveyor = []

    def transport_item(self, item):

        self.items_on_conveyor.append(item)
        print(f"Item transported on Conveyor {self.name}: {item}")

